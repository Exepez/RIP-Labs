from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import json
from tabulate import tabulate

class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self,path) -> None:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        result = self._strategy.do_algorithm(data)
        best=[]
        for i in range(0,5): 
            best.append(result[i])
        print ("\n        Лучший отель:")
        print ("Название:           "+result[0]['name'])
        print ("Стоимость за день:  "+str(result[0]['costperday']))
        print ("Звезды:             "+str(result[0]['star']))
        print ("Цена за звезду:     "+str(result[0]['starcost']))
        print ("\n             Топ лучших отелей:")
        print (tabulate(best, headers='keys', tablefmt="fancy_grid"))
        return result[0]['name']



class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data, key=lambda k: k['star'], reverse = True)
        

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return sorted(data, key=lambda k: k['costperday']) 


class ConcreteStrategyC(Strategy):
    def do_algorithm(self, data):
        return sorted(data, key=lambda k: k['starcost']) 


if __name__ == "__main__":

    path = 'data_light.json'
    context = Context(ConcreteStrategyA())
    print("\n\nКлиент: Лучший отель по звездам")
    context.do_some_business_logic(path)
    print()

    print("\n\nКлиент: Лучший отель по цене")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic(path)

    print("\n\nКлиент: Лучший отель по цене за звезду")
    context.strategy = ConcreteStrategyC()
    context.do_some_business_logic(path)