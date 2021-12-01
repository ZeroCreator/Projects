# Рисуем правильные многоугольники turtrle.
import turtle
pen = turtle.Turtle()
pen.speed(10)
pen.up()
pen.setposition(-30, -30)
pen.down()
colors = ['red', 'brown', 'green', 'blue']

def righMNOG(n, dlina):
    sumAngle = (n - 2) * 180
    if sumAngle % n == 0:
        angle = sumAngle // n
        for i in range(n):
            pen.forward(100)
            pen.left(180 - angle)


for i in range(3, 11):
    pen.color(colors[i % 4])
    righMNOG(i, 50)

