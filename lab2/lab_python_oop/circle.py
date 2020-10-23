from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    Type = "Круг"

    def getType(self):
        return self.Type

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fcolor = FigureColor()
        self.fcolor.colorprop = color_param

    def square(self):
        return math.pi*(self.r**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.getType(),
            self.fcolor.colorprop,
            self.r,
            self.square()
            )