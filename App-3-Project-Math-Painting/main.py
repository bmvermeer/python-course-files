from canvas import Canvas
from shapes import Rectangle, Square

canvas_w = int(input("Canvas width: "))
canvas_h = int(input("Canvas height: "))

colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Canvas color (black or white): ")

canvas = Canvas(canvas_w, canvas_h, colors[canvas_color])

shape_colors = {"red": (255,0,0), "blue": (0,0,255), "green": (0,255,0), "yellow": (255,255,0), "orange": (255,128,0), "purple": (255,0,255)}

def draw_rectangle():
    rect_x = int(input("Rectangle X: "))
    rect_y = int(input("Rectangle Y: "))
    rect_width = int(input("Rectangle width: "))
    rect_height = int(input("Rectangle heigth: "))
    rect_color = input("Rectangle Color (red, blue, green, yellow, orange, purple: ")
    rectangle1 = Rectangle(rect_x, rect_y, rect_width, rect_height, shape_colors[rect_color])
    rectangle1.draw(canvas)

def draw_square():
    sq_x = int(input("Square X: "))
    sq_y = int(input("Square Y: "))
    sq_side = int(input("Square side: "))
    sq_color = input("Square Color (red, blue, green, yellow, orange, purple: ")
    square1 = Square(sq_x, sq_y, sq_side, shape_colors[sq_color])
    square1.draw(canvas)

while True:
    shape = input("What do you want to draw (rectangle | square | quit): ")
    if shape.lower() == "rectangle":
        draw_rectangle()
    if shape.lower() == "square":
        draw_square()
    if shape.lower() == "quit":
        break


canvas.make("canvas.png")




# canvas = Canvas(20, 30, (255, 255, 255))
# rectangle1 = Rectangle(1, 6, 7, 10, (0, 0, 255))
# rectangle1.draw(canvas)
#
# square1 = Square(5, 15, 8, (0, 255, 0))
# square1.draw(canvas)
#
# canvas.make("canvas.png")


