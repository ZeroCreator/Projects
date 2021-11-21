"""
Задание 3:
Создайте функцию, которая определяет, представляет ли ввод «stalactites» (сталактиты) или «stalagmites» (сталагмиты).
Если ввод содержит и сталактиты, и сталагмиты, верните «both» («оба»).
Ввод будет двухмерным списком, где 1 представляет кусок камня, а 0 — воздушное пространство.

mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
"""


def mineralFormation(mas):
    stalactites = 0
    stalagmites = 0
    for i in mas[0]:
        if i == 1:
            stalactites = 1

    for i in mas[-1]:
        if i == 1:
            stalagmites = 1

    if stalactites and stalagmites:
        return "both"
    if stalactites:
        return "stalactites"
    if stalagmites:
        return "stalagmites"


#
# def mineral_formation(input):
#     if 1 in input[0] and 1 in input[-1]:
#         return 'both'
#     if 1 in input[0] :
#         return 'stalactites'
#     if 1 in input[-1]:
#         return 'stalagmites'


p1 = mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
])

print(p1)

p2 = mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])

print(p2)

p3 = mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])
print(p3)


p4 = mineralFormation([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
])
print(p4)



