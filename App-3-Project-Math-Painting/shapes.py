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
