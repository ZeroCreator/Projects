def change_list(a_list):
    a_list = [1, 2, 3]
    return a_list


main_list = []
change_list(main_list)
print(main_list)

class Cat:

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    cat1 = Cat('Tom')
    cat2 = Cat('Tom')
    print(cat1 == cat2)


var = 1,
var_2 = (1)
print(type(var))
print(type(var_2))

#a_tuple = (1, 2, [3, 4])
#a_tuple[2] += [5]
#print(a_tuple)

a_dict = {}
a_dict[1] = 'foo'
a_dict[True] = 'bar'
print(a_dict)



"""
def is_pandigital(m):
    if sorted(set([i for i in m])) == list('0123456789'):   # is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False

print(is_pandigital(input()))
"""

def is_pandigital(m):
    if sorted(set([i for i in input()])) == list('0123456789'):   # is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False

is_pandigital()


def harry(ls: list) -> int:
    n = len(ls)
    m = len(ls[0])
    d = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = ls[i-1][j-1] + max(d[i-1][j], d[i][j-1])
    maximum_result = d[-1][-1]
    return -1 if maximum_result == 0 else maximum_result




print(harry([[5, 2], [5, 2]]))
print(harry([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
print(harry([[]]))