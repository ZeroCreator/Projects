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



