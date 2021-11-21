"""
Лабиринт
"""
import copy
from tkinter import *
from tkinter.messagebox import showinfo
from random import randint
import time
# Функция считает для каждого слота возможные пути
def count_mine(mine_map_end):
    while True:
        temp = copy.deepcopy(mine_map_end)
        for row in range(0, ROW):
            for col in range(0, COLUMNS):
                # Проверяем что записано в текущем слоте на котором мы 'стоим'
                k = mine_map_end[row][col]
                # Если мы находимся на слоте который стена или на слоте который пустой(кроме начального)
                # то пропускаем эту итерацию цикла.
                if mine_map_end[row][col] == 'X' or (k == 0 and row + col != 0):
                    continue
                # Перебираем смещения(по строкам и столбцам)  относительно слота где мы стоим.
                for (dx, dy) in (0, 1), (1, 0), (-1, 0), (0, -1):
                    # Проверяем не выходит ли соседний слот за границы матрицы.
                    if any((col+dx < 0, col+dx > COLUMNS - 1, row+dy < 0, row+dy > ROW-1,
                            (row+dy == 0 and col+dx == 0))):
                        continue
                    # Проверяем не является ли соседний слот стеной и нет там ли цифры кроме нуля.
                    if mine_map_end[row + dy][col + dx] != 'X' and mine_map_end[row + dy][col + dx] == 0:
                        # Прибавляем в соседний слот 1(по умолч там 0)
                        mine_map_end[row + dy][col + dx] = k + 1
        return mine_map_end if mine_map_end == temp else count_mine(mine_map_end)
def output_exit(mine_map_end, buttons):
    way_exit = []
    path_end = tuple()
    max_step = 0
    # Выводим в слоты рассчитанные значения шагов для каждого слота(для отладки)
    for ind_row, row in enumerate(mine_map_end):
        for ind_col, col in enumerate(row):
            buttons[ind_row][ind_col].config(text=col)
            if type(col) is int:
                if col > max_step:
                    max_step = col
                    path_end = ((ind_row, ind_col))
    if not path_end:
        buttons[0][0].config(bg='Red')
        return
    if mine_map_end[ROW-1][COLUMNS-1] == 0 or mine_map_end[ROW-1][COLUMNS-1] == 'X':
        way_exit.append((path_end[0], path_end[1]))
        max_count_step = max_step
        exit_map = False
    else:
        max_count_step = mine_map_end[ROW-1][COLUMNS-1]
        path_end = ((ROW-1, COLUMNS-1))
        way_exit.append((path_end[0], path_end[1]))
        exit_map = True
    row = path_end[0]
    col = path_end[1]
    for current_step in range(max_count_step, -1, -1):
        color = 'Green' if exit_map else 'Red'
        buttons[row][col].config(bg=color)
        for (dx, dy) in (0, 1), (1, 0), (-1, 0), (0, -1):
            # Проверяем не выходит ли соседний слот за границы матрицы.
            if any((col+dx < 0, col+dx > COLUMNS-1, row+dy < 0, row+dy > ROW-1)):
                continue
            if mine_map_end[row+dy][col+dx] == current_step-1:
                way_exit.append((row+dy, col+dx))
                row = row + dy
                col = col + dx
    buttons[ROW-1][COLUMNS-1].config(font='Calibre 9 bold', text='exit', fg='Red')
    buttons[0][0].config(text='start', fg='Blue')
def click_on_button_start(mine_map, buttons, btn_help, btn_next):
    output_exit(count_mine(mine_map), buttons)
    btn_help.config(state=DISABLED)
    btn_next.config(state=NORMAL)
# Функция создания случайным образом лабиринта.
# Генерируем матрицу(двухмерный список) со случайными высотой и длиной(в зависимости от сложности игры),
# со случайным количеством и расположением "стен" в матрице.
def generator_map():
    # Случайная высота и длина  матрицы (карты лабиринта)
    row = columns = randint(7, 15)
    # Непосредственно генерируем матрицу в которой расставляем случайным образом
    #  (застены, записываем в эти слоты '#'), в остальных слотах записываем '0'.
    mine_map = [[0 if randint(0, 100) > 25 else 'X' for j in range(0, columns)]
                for i in range(0, row)]
    mine_map[0][0] = 0
    # Возвращаем сгенерированное поле.
    return mine_map
# Главная функция MINEMAP()
def MINEMAP() -> None:
    # Формируем игровое окно
    window = Tk()
    window.title('Лабиринт')
    # Создаем меню
    main_menu = Menu(window)
    window.config(menu=main_menu)
    main_menu.add_command(label='Выход', command=quit)
    main_menu.add_separator()
    # Создаем две рамки (Frame) в которую поместим упаковщиком pack() виджеты - надписи(label) и
    # кнопки(Button) для перебора "минных карт" и кнопку "HELP"
    frame = Frame()
    frame.pack(side=TOP, fill=X, expand=True)
    Label(frame, text=f'{40 * " "}ЛАБИРИНТ{40 * " "}', font='Arial 11').pack(pady=3)
    frame = Frame()
    frame.pack(side=TOP)
    btn_next = Button(frame,  state=DISABLED, text="Next map", font='Calibre 10 bold', command=window.destroy)
    btn_next.grid(row=0, column=0, padx=50, pady=5)
    btn_help = Button(frame, text="  START  ")
    btn_help.config(font='Calibre 10 bold', command=lambda: click_on_button_start(MINE_MAP, buttons, btn_help, btn_next))
    btn_help.grid(row=0, column=1, padx=50, pady=5)
    # Создаем новую рамку (Frame) в которую поместим упаковщиком grid() матрицу из кнопок которая
    # и будет нам картой.
    frame = Frame()
    frame.pack(side=TOP)
    # В этом списке будем хранить объекты кнопок(матрица)
    buttons = []
    for rows in range(ROW):
        temp = []
        for col in range(COLUMNS):
            # Под каждый слот матрицы создаем экземпляр кнопки (каждая кнопка имеет определенный цвет фона).
            btn = Button(frame)
            btn.config(bd=1, width=3, height=1, font='Calibre 9 bold')
            if MINE_MAP[rows][col] == 'X':
                btn.config(activebackground='Red', text='X', bg='Black', fg='Red')
            else:
                btn.config(activebackground='White', bg='White', fg='Black')
            temp.append(btn)  # формируем строку из объектов кнопок для матрицы
            btn.grid(row=rows, column=col)  # упаковываем кнопки во фрейм упаковщиком grid()
        buttons.append(temp)  # добавляем в матрицу строку из объектов кнопок
    buttons[ROW-1][COLUMNS-1].config(text='exit', fg='Red')
    buttons[0][0].config(text='start', fg='Blue')
    Label(frame, height=4, fg="White").grid(row=ROW, column=COLUMNS-1)  # делаем отступ для карты снизу
    # Размещаем наше графич. окно в центре, для этого нужно высчитать размеры окна после
    # размещения на ней всех виджетов(оно каждый раз будет новым в зависимости от размера матрицы).
    # Обновляем окно когда все элементы размещены(чтобы высчитать его размер).
    window.update_idletasks()
    # Рассчитываем размеры окна
    s = window.geometry()  # 384x405+104+104  # полные параметры окна(размеры 384x405 и начало координат +104+104)
    s = s.split('+')  # ['384x405', '104', '104']  # отделяем размеры окна от начало координат
    s = s[0].split('x')  # ['384', '405']  - вычленяем отдельно размеры(ширину и высоту) сформированного окна
    width_window = int(s[0])  # Ширина окна
    height_window = int(s[1])  # Высота окна
    # Размещаем наше графич. окно в центре экрана.
    x_start = (window.winfo_screenwidth() - width_window) // 2  # высчитываем начало окна по горизонтали
    y_start = (window.winfo_screenheight() - height_window) // 2  # высчитываем начало окна по вертикали
    # window.wm_geometry(f'+{0}+{0}')  # выводим окно с верхнего левого угла (0,0)
    window.wm_geometry(f'+{x_start}+{y_start}')  # выводим окно в центре
    window.resizable(width=False, height=False)  # можно запретить изменять окно размеры
    mainloop()
# Запускается основная программа
if __name__ == "__main__":
    # Генерируем разные матрицы покуда не выберем 'Выход' из программы
    while True:
        # Вызываем функцию генерирования поля.
        MINE_MAP = generator_map()
        ROW = len(MINE_MAP)
        COLUMNS = len(MINE_MAP[0])
        # Вызываем функцию окна.
        MINEMAP()