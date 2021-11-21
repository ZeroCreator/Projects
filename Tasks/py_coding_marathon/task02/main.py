# def normalize(text_sentence):
#     if text_sentence[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         return f"{text_sentence.capitalize()}!"
#     return text_sentence


def normalize(txt):
    if txt.isupper()==True:
        txt = txt.capitalize()+"!"
    return txt


if __name__ == '__main__':
    print(normalize("CAPS LOCK DAY IS OVER"))
    print(normalize("Today is not caps lock day."))
    print(normalize("Let us stay calm, no need to panic."))