# Баран (Кривая Леви)

from turtle import *

def main():
    init_turtle()
    forward_krivo(100, 10)


    hideturtle()

def init_turtle():
    shape('turtle')
    penup()
    goto(-100, 100)
    pendown()
    shapesize(2)
    speed(100)
    color('green', 'yellow')

def forward_krivo(l, n):
    if n == 0:
        forward(l)
    else:
        left(45)
        forward_krivo(l/2**0.5, n - 1)
        right(90)
        forward_krivo(l/2**0.5, n - 1)
        left(45)


main()