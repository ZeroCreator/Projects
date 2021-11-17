# Программа для ведения списка дел.
# Функциональность:
# Запрашивать у пользователя команду
# В зависимости от введенной команды выполнять действие
# random - добавлять случайную задачу на дату Сегодня
# Команды:
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашиваем у пользователя)
# show - напечатать все добавленные задачи
import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
"""

RANDOM_TASKS = ["Поучить Python", "Порисовать", "Потанцевать", "Поспать"]
tasks = {}

run = True

def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаем запись с ключем date
        tasks[date] = []
        tasks[date].append(task)
    print(f"Задача {task} добавлена на дату {date}")


while run:
    command = input("Ведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print("- ", task)
        else:
            print("Нет задач на эту дату")
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        break
    else:
        print("Неизвестная команда")
        break


print("Программа завершена.")