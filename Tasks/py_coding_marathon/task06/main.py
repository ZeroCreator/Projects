def harry(two_dimensional_list: list) -> int:
    """ Функция рассчитывает накопительную сумму значений ячеек в матрице с высотой n и длиной m от (0,0) к (n-1, m-1).
    :param two_dimensional_list: матричный двумерный список
    :return: максимальная сумма значений, если список не пустой, иначе -1
    """
    n = len(two_dimensional_list)
    m = len(two_dimensional_list[0])
    computed_array = [[0 for i in range(m + 1)] for j in range(n + 1)]   # Создаем матрицу для рассчета с высотой n+1 и длиной m+1 и заполняем ее нулями.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            computed_array[i][j] = two_dimensional_list[i - 1][j - 1] + max(computed_array[i - 1][j],
                                                                            computed_array[i][j - 1]) # Заполняем матрицу по формуле рассчета максимально возможной суммы значений
    maximum_result = computed_array[-1][-1]
    return -1 if maximum_result == 0 else maximum_result



if __name__ == "__main__":
    assert harry([[5, 2], [5, 2]]) == 12
    assert harry([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 72
    assert harry([[]]) == -1



print(harry([[5, 2], [5, 2]]))
print(harry([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]))
print(harry([[]]))

