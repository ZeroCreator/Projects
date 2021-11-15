"""
Задача 5
Напишите функцию, которая возвращает True, если в переданном числе за каждой последовательностью единиц следует
последовательность нулей той же длины.
Примеры:
same_length (110011100010) ➞ True
same_length (101010110) ➞ False
same_length (111100001100) ➞ True
same_length (111) ➞ False
"""


def same_length(incoming_number: int) -> bool:
    """Функция определяет следует ли в переданном числе за каждой последовательностью единиц последовательность нулей той же длины.
    :param incoming_number: вводимое число из единиц и нулей
    :return: True or False
    """
    list_units = list(filter(None, str(incoming_number).split("0")))
    list_zeros = list(filter(None, str(incoming_number).split("1")))
    return [len(i) for i in list_units] == [len(i) for i in list_zeros]



# t = same_length(110011100010)
# t1 = same_length(101010110)
# t2 = same_length(111100001100)
# t3 = same_length(111)
# t4 = same_length(000)
#
# print(t)
# print(t1)
# print(t2)
# print(t3)
# print(t4)

# def same_length(incoming_number, first_digit="1", second_digit="0"):
#     list_units = list(filter(None, str(incoming_number).split(second_digit)))
#     list_zeros = list(filter(None, str(incoming_number).split(first_digit)))
#     return [len(i) for i in list_units] == [len(i) for i in list_zeros]
#
#
#
# t = same_length(110011100010)
# t1 = same_length(101010110)
# t2 = same_length(111100001100)
# t3 = same_length(111)
# t4 = same_length(000)
#
# print(t)
# print(t1)
# print(t2)
# print(t3)
# print(t4)



if __name__ == "__main__":
    assert same_length(110011100010)
    assert not same_length(101010110)
    assert same_length(111100001100)
    assert not same_length(111)
    assert not same_length(000)
    assert not same_length(1)
    assert not same_length(110100)


