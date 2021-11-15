# Кривая "Дракон"
from turtle import *

def main():
    init_turtle()
    forward_krivo(100, 10)


    hideturtle()

def init_turtle():
    shape('turtle')
    penup()
    goto(-100, -100)
    pendown()
    shapesize(2)
    speed(100)
    color('green', 'yellow')

def forward_krivo(l, n, sign=1):
    if n == 0:
        forward(l)
    else:
        left(sign*45)
        forward_krivo(l/2**0.5, n - 1, -1)
        right(sign*90)
        forward_krivo(l/2**0.5, n - 1)
        left(sign*45)


main()