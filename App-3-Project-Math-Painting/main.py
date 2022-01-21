
from PIL import Image
import numpy


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:(self.x + self.side), self.y : (self.y + self.side)] = self.color


    def __str__(self):
        return f'Square [x={self.x} y={self.y} side={self.side} color={self.color}]'


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:(self.x + self.height), self.y:(self.y + self.width)] = self.color

    def __str__(self):
        return f'Rectangle [x={self.x} y={self.y} width={self.width} height={self.height} color={self.color}]'


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = numpy.zeros((self.width, self.height, 3), dtype=numpy.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


canvas = Canvas(20, 30, (255, 255, 255))
rectangle1 = Rectangle(1, 6, 7, 10, (0, 0, 255))
rectangle1.draw(canvas)

square1 = Square(5, 15, 8, (0, 255, 0))
square1.draw(canvas)

canvas.make("canvas.png")


