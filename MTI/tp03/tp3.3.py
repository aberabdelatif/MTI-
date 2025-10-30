class Shape:
    def get_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def get_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    ar = Rectangle(12,3)
    sq = Square(5)
    print({ar.get_area()})
    print({sq.get_area()})
    