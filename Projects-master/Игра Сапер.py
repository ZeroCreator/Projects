"""
Игрок может открывать любую клетку поля и если там нет мины, то показывается число о количестве мин в
прилегающих клетках.Цель – открыть все поле не задев мин.
"""
import random

N, M = (5, 10) # размер игрового поля

def startGame():
    """Функция запуска игры: отображается игровое поле,
            игрок открывает любую закрытую клетку,
            результат проверяется на наличие мины или
            выигрышной ситуации
        """
P = [-2]*N*N
PM = [0]*N*N
"""
Здесь у поля P значение -2 будет говорить о том, что клетка еще не открыта. Значение -1 у поля PM – стоит мина, 
а любое неотрицательное число у обоих списков – открытая клетка без мины и указанием мин вокруг нее.
"""

    createGame(PM)
    finishState = isFinish(PM, P)
    while finishState > 0:
        show(P)
        x, y = goPlayer()

        P[x * N + y] = PM[x * N + y]
        finishState = isFinish(PM, P)

    return finishState

    while isFinish():
        show()
        goPlayer()

res = startGame()
if res == -1:
    print("Вы проиграли")
else:
    print("Вы выиграли")

    def show():
        """Функция отображения состояния текущего
                игрового поля
            """
        for i in range(N):
            for j in range(N):
                print(str(pole[i*N + j]).rjast(3), end="")

    def createGame(PM):
        """Создание игрового поля: расположение мин
                и подсчет числа мин вокруг клеток без мин
                если клетка имеет значение >= 0, то мины в ней нет
                и число показывает количество мин вокруг текущей клетки.
                А любое отрицательное значение – мина есть.
            """
        rnd = random.Random()
        n = M
        while n > 0:
            i = rnd.random(N) # случайное целое [0; N)
            j = rnd.random(N)
            if PM[i*N + j] != 0:
                continue
            PM[i*N + j] = -1
            n -= 1

        # вычисляем количество мин вокруг клетки
        for i in range(N):
            for j in range(N):
                if PM[i*N + j] >= 0:
                    PM[i*N + j] = getTotalMines(PM, i, j)

        def getTotalMines(PM, i, j):
            n = 0
            for k in range(-2, 2):
                for l in range(-1, 2):
                    x = i + k
                    y = j + l
                    if x < 0 or x >= N or y < 0 or y >= N:
                        continue
                    if PM[x*N + y] < 0:
                        n += 1

            return

    def goPlayer():
        """Функция для ввода пользователем координат
                закрытой клетки игрового поля
            """
        flLoopInput = True
        while flLoopInput:
            x, y = input("Введите координату через пробел: ").split()
            if not x.isdigit() or not y.isdigit():
                print("Координаты введены неверно")
                continue

            x = int(x) - 1
            y = int(y) - 1

            if x < 0 or x >= N or y < 0 or y >= N:
                print("Координаты выходят за пределы поля")
                continue

            flLoopInput = False

        return (x, y)

    def isFinish():
        """Определение текущего состояния игры:
                выиграли, проиграли, игра продолжается
                если функция возвращает:
         1 – игра продолжается;
        -1 – игрок наступил на мину и игра проиграна;
        -2 – игрок открыл все клетки без мин – игра выиграна.
            """
        for i in range(N * N):
            if P[i] != -2 and PM[i] < 0: return -1
            if P[i] == -2 and PM[i] >= 0: return 1

        return -2



createGame(PM)
show(PM)
goPlayer()

startGame()
print("Игра завершена")

print(help(startGame))