#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import abc

class Shape:
    def draw(self):
        pass
    
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


if __name__ == "__main__":
    last_shape = None

    for t in ("Circle", "Square", "Circle", "Square"):
        if t == "Circle":
            last_shape = Circle()
        elif t == "Square":
            last_shape = Square()
        else:
            print("Bad shape creation:", t)

    
    last_shape.draw()
    last_shape.erase()

    sys.exit()
