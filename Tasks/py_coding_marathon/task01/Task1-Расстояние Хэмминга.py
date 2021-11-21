"""
Задание 1:
Создайте функцию, которая принимает две строки и вычисляет расстояние Хэмминга между ними.
Расстояние Хэмминга — число позиций, в которых соответствующие символы двух слов одинаковой длины различны.
Например, в строке «ABCB» на четвертой позиции стоит буква «B», а в строке «ABCD» на той же позиции — буква «D».
Расстояние Хэмминга между этими строками — 1.
Примечание: Исходим из того, что передаваемые строки всегда будут одинаковой длины.
Примеры:
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
hamming_distance("ABBA", "abba") ➞ 4
"""


def hamming_distance(a, b):
    first_str = list(a)
    second_str = list(b)
    count = 0

    for i in range(len(first_str)):
        if first_str[i] != second_str[i]:
            count += 1

    return count

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
print(hamming_distance("ABBA", "abba"))

"""
def hamming_distance(string_1:str, string_2:str) -> int:
    distance = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            distance += 1
    return distance

"""