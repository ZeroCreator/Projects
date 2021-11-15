# Черепашка (Кривые Коха - Снежинка Коха)
from turtle import *

def main():
    init_turtle()
    for adge in range(3):
        forward_krivo(200, 4)
        right(120)

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
        forward_krivo(l / 3, n - 1)
        left(60)
        forward_krivo(l / 3, n - 1)
        right(120)
        forward_krivo(l / 3, n - 1)
        left(60)
        forward_krivo(l / 3, n - 1)

main()