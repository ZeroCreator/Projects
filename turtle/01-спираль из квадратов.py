# Рисунок в виде спирали из квадратов

import turtle

def sq(a):
    for i in range(4):
        joe.color(colors[i % 4])
        joe.forward(a)
        joe.left(90)

colors = ['red', 'brown', 'green', 'blue']

joe = turtle.Turtle()
joe.speed(100)

dlina = 30

for i in range(60):
    # joe.color(colors[i%4])
    sq(dlina) # Фрактал квадратов
    # joe.circle(dlina) # Фрактал кругов
    joe.right(10)
    dlina += 4
