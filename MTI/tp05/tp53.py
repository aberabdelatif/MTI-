#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

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


# 2D Circle
class Circle2D(Circle):
    def draw(self):
        print("Circle2D.draw")

    def erase(self):
        print("Circle2D.erase")


# 3D Circle
class Circle3D(Circle):
    def draw(self):
        print("Circle3D.draw")

    def erase(self):
        print("Circle3D.erase")



class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


# 2D Square
class Square2D(Square):
    def draw(self):
        print("Square2D.draw")

    def erase(self):
        print("Square2D.erase")


# 3D Square
class Square3D(Square):
    def draw(self):
        print("Square3D.draw")

    def erase(self):
        print("Square3D.erase")

class ShapeFactory(ABC):
    @abstractmethod
    def createShape(self, shape_type):
        pass




class ShapeFactory2D(ShapeFactory):
    def createShape(self, shape_type):

        if shape_type == "Circle":
            return Circle2D()

        elif shape_type == "Square":
            return Square2D()

        else:
            print("Bad 2D shape creation:", shape_type)
            return None


class ShapeFactory3D(ShapeFactory):
    def createShape(self, shape_type):

        if shape_type == "Circle":
            return Circle3D()

        elif shape_type == "Square":
            return Square3D()

        else:
            print("Bad 3D shape creation:", shape_type)
            return None




if __name__ == "__main__":

    
    factories = {
        "2D": ShapeFactory2D(),
        "3D": ShapeFactory3D()
    }

    
    for dim in ("2D", "3D"):
        for shape in ("Circle", "Square"):
            print(f"\n--- Creating {shape} {dim} ---")
            obj = factories[dim].createShape(shape)
            obj.draw()
            obj.erase()
