from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def setEngine(self) -> None:
        pass

    @abstractmethod
    def setFuel(self) -> None:
        pass

    @abstractmethod
    def setMTransmission(self) -> None:
        pass

    @abstractmethod
    def setATransmission(self) -> None:
        pass

    @abstractmethod
    def setConditioner(self) -> None:
        pass

    @abstractmethod
    def setOnBoardComp(self) -> None:
        pass

    @abstractmethod
    def setFogLights(self) -> None:
        pass


class ConcreteBuilderCar(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = ProductCar()

    @property
    def product(self) -> ProductCar:
        product = self._product
        self.reset()
        return product

    def setEngine(self) -> None:
        self._product.add("Двигатель легкового автомобиля")

    def setFuel(self) -> None:
        self._product.add("Бензин")

    def setMTransmission(self) -> None:
        self._product.add("МКП")
        return True

    def setATransmission(self) -> None:
        self._product.add("АКП")

    def setConditioner(self) -> None:
        self._product.add("Кондиционер")
    
    def setOnBoardComp(self) -> None:
        self._product.add("Бортовой компьютер")

    def setFogLights(self) -> None:
        self._product.add("Противотуманные фары")

class ConcreteBuilderTruck(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = ProductTruck()

    @property
    def product(self) -> ProductTruck:
        product = self._product
        self.reset()
        return product

    def setEngine(self) -> None:
        self._product.add("Двигатель грузового автомобиля")

    def setFuel(self) -> None:
        self._product.add("Дизель")

    def setMTransmission(self) -> None:
        self._product.add("МКП")
        return True

    def setATransmission(self) -> None:
        self._product.add("АКП")

    def setConditioner(self) -> None:
        self._product.add("Кондиционер")
    
    def setOnBoardComp(self) -> None:
        self._product.add("Бортовой компьютер")

    def setFogLights(self) -> None:
        self._product.add("Противотуманные фары")

class ProductCar():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Комплектация легкового автомобиля: {', '.join(self.parts)}", end="")
        return f"{', '.join(self.parts)}"

class ProductTruck():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Комплектация грузового автомобиля: {', '.join(self.parts)}", end="")
        return f"{', '.join(self.parts)}"

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_basic(self) -> None:
        print("Базовая конфигурация автомобиля (Basic): ")
        self.builder.setEngine()
        self.builder.setFuel()
        self.builder.setMTransmission()

    def build_standart(self) -> None:
        print("Стандартная конфигурация автомобиля (Standart): ")
        self.builder.setEngine()
        self.builder.setFuel()
        self.builder.setATransmission()
        self.builder.setConditioner()
    
    def build_advanced(self) -> None:
        print("Раcширенная конфигурация автомобиля (Advanced): ")
        self.builder.setEngine()
        self.builder.setFuel()
        self.builder.setATransmission()
        self.builder.setConditioner()
        self.builder.setOnBoardComp()
        self.builder.setFogLights()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilderCar()
    director.builder = builder

    # print("Базовая конфигурация автомобиля (Basic): ")
    director.build_basic()
    builder.product.list_parts()

    print("\n")

    # print("Стандартная конфигурация автомобиля (Standart): ")
    director.build_standart()
    builder.product.list_parts()

    print("\n")\

    # print("Раcширенная конфигурация автомобиля (Advanced): ")
    director.build_advanced()
    builder.product.list_parts()

    print("\n")

    builder = ConcreteBuilderTruck()
    director.builder = builder

    print("Собранная конфигурация автомобиля (Custom): ")
    builder.setEngine()
    builder.setFuel()
    builder.setMTransmission()
    builder.setConditioner()
    builder.setFogLights()
    builder.product.list_parts()