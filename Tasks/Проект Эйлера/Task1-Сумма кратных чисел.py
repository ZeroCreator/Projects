# Задача 1.
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3б 5б 6 и 9.
# Сумма этих чисел равна  23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''
print('С помощью цикла while')
sum = 0 # сумма
b = 0 # счетчик
while b < 1000:
    if b % 3 == 0 or b % 5 == 0:
       sum += b
    b += 1
print(sum)
'''

print('С помощью генератора списков')
print(sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))

print('С помощью цикла for')
s = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)

print('С помощью функции')
def compute():
    ans = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return str(ans)

if __name__ == '__main__':
    print(compute())


