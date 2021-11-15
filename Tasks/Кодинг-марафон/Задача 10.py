from random import choice
a = ["В этом лабиринте одни тупики!", "Выход так близко, но недостижим!", "Выхода нет!"]

def can_exit(lst: list) -> list:
    flag: int = 3
    if lst[0][0] == 0:
        lst[0][0] = flag
    for i in range(len(lst)-1):
        for j in range(len(lst[i])):
            if lst[i][j] == flag:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if i + x >= 0 and j + y >= 0 and i + x < len(lst) and j + y < len(lst[i]):
                            if lst[i + x][j + y] == 0:
                                lst[i + x][j + y] = flag
            lst[i][j] = 0
    if lst[-1][-1] == flag:
        return True
    else:
        return choice(a)
    # return lst[-1][-1] == flag else choice(a)



print(can_exit([
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 0]
]))


print(can_exit([
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1]
]))

print(can_exit([
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1]
]))

print(can_exit([
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0]
]))

print(can_exit([
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0]
]))

print(can_exit([
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0]
]))