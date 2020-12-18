import unittest
from stroitel import *

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.director=Director()
       
    def test_setEngine(self):
        builder = ConcreteBuilderCar()
        director = Director()
        director.builder = builder
        builder.setEngine()
        self.assertEqual(builder.product.list_parts(), "Двигатель легкового автомобиля")
        print("\n")
        builder = ConcreteBuilderTruck()
        director.builder = builder
        builder.setEngine()
        self.assertEqual(builder.product.list_parts(), "Двигатель грузового автомобиля")
        print("\n")

    def test_build_config(self):
        director = Director()
        builder = ConcreteBuilderCar()
        director.builder = builder

        director.build_standart()
        self.assertEqual(builder.product.list_parts(), "Двигатель легкового автомобиля, Бензин, АКП, Кондиционер")
        print("\n")

        director.build_basic()
        self.assertEqual(builder.product.list_parts(), "Двигатель легкового автомобиля, Бензин, МКП")
        print("\n")

        director.build_advanced()
        self.assertEqual(builder.product.list_parts(), "Двигатель легкового автомобиля, Бензин, АКП, Кондиционер, Бортовой компьютер, Противотуманные фары")
        print("\n")

    def test_setMTransmission(self):
        director = Director()
        builder = ConcreteBuilderCar()
        director.builder = builder
        self.assertTrue(builder.setMTransmission())

        
if __name__ == '__main__':
    unittest.main()