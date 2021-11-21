Задача №7.
У нас есть список названий животных:

animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]
           
Напишите функцию, которая будет принимать строку txt и возвращать максимальное количество
названий животных, которые возможно собрать из символов строки.

txt = "goatcode"

count_animals(txt) ➞ 2
(первое животное = "dog", оставшиеся символы в строке = "atcoe", второе животное = "cat". count = 2 (верно), если взять  сперва  "goat", оставшиеся символы в строке = "code", т.е. больше нельзя составить имен животных count = 1 (неверно))

Еще примеры
count_animals("goatcode") ➞ 2 # "dog", "cat"

count_animals("cockdogwdufrbir") ➞ 4 # "cow", "duck", "frog", "bird"

count_animals("dogdogdogdogdog") ➞ 5
