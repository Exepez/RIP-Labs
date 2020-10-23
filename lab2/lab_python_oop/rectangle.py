from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    Type = "Прямоугольник"

    def getType(self):
        return self.Type

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fcolor = FigureColor()
        self.fcolor.colorprop = color_param

    def square(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format (
            self.getType(), 
            self.fcolor.colorprop, 
            self.width, 
            self.height, 
            self.square()
            )