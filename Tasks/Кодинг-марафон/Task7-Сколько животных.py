"""
Задача №7.
У нас есть список названий животных:
animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]
Напишите функцию, которая будет принимать строку txt и возвращать максимальное количество
названий животных, которые возможно собрать из символов строки.
txt = "goatcode"
count_animals(txt) ➞ 2
# первое животное = "dog"
# оставшиеся символы в строке = "atcoe",
# второе животное = "cat".
# count = 2 (верно)
# если взять  сперва  "goat",
# оставшиеся символы в строке = "code",
# т.е. больше нельзя составить имен животных
# count = 1 (неверно)
Еще примеры
count_animals("goatcode") ➞ 2
# "dog", "cat"
count_animals("cockdogwdufrbir") ➞ 4
# "cow", "duck", "frog", "bird"
count_animals("dogdogdogdogdog") ➞ 5
"""

animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]


def count_animals(txt):
    counts = []
    def f(txt, c):
        for i in animals:
            s = txt
            for x in i:
                s = s.replace(x, "", 1)
            if len(s) + len(i) == len(txt):
                f(s, c + 1)
        counts.append(c)
    f(txt, 0)
    return max(counts)