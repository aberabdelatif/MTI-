#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def erase(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")
class triangle(Shape):
    def draw(self):
        print("triangle.draw")

    def erase(self):
        print("triangle.erase")

class rectangle(Shape):
    def draw(self):
        print("rectangle.draw")

    def erase(self):
        print("rectangle.erase")

class Square(Shape):
    def draw(self):
        print("Squar.draw")

    def erase(self):
        print("Squar.erase")


class ShapeFactory:
    @staticmethod
    def createShape(type):
        if type == "Circle": return Circle()
        elif type == "Square": return Square()
        else:
            print("Bad shape creation: " + type)

        sys.exit()
if __name__ == "__main__":
    for type in ("Circle", "Square" ,"Circle", "Square"):
        shape = ShapeFactory.createShape(type)
shape.draw()
shape.erase()