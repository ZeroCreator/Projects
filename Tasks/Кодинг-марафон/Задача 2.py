"""
Задание 2:
22 октября — ДЕНЬ CAPS LOCK. За исключением этого дня, все предложения должны быть в нижнем регистре. Поэтому напишите
функцию для нормализации предложения.
Эта функция должна принимать строку. Если строка состоит только из символов верхнего регистра, переведите их в нижний
регистр и добавьте в конце восклицательный знак.
Примечания:
- каждая передаваемая в функцию строка - отдельное предложение
- предложение после нормализации должно начинаться с заглавной буквы
- восклицательный знак добавляем к предложениям, которые переводили из верхнего регистра в нижний.
Примеры:
normalize("CAPS LOCK DAY IS OVER")
➞ "Caps lock day is over!"
normalize("Today is not caps lock day.")
➞ "Today is not caps lock day."
normalize("Let us stay calm, no need to panic.")
➞ "Let us stay calm, no need to panic."
"""


# def normalize(text_sentence):
#     if text_sentence[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         return f"{text_sentence.capitalize()}!"
#     return text_sentence


def normalize(txt):
    if txt.isupper()==True:
        txt = txt.capitalize()+"!"
    return txt


print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("Let us stay calm, no need to panic."))