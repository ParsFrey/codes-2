import turtle
import time

x = turtle.Turtle()
x.shape('turtle')

x.speed(50)

while True:
    x.forward(100)
    x.right(90)

    a=0
    while a<4:
        x.forward(50)
        x.right(90)
        a += 1
        while a<2:
            x.forward(50)
            x.right(85)
            a += 1   
