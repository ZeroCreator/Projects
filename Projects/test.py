"""
n = list(map(str, input().split()))
s = []
for i in n:
    s.append(i.lower())

d = s[0][-1]


for i in s[1:]:
    if i[-1] == 'ь' or i[-1] =='ъ' or i[-1] == 'ы':
        i[-1] == i[-2]
        if i[0] == d:
            print("ДА")
            break
    else:
        print("НЕТ")
"""
"""
n = input()
s = []
for i in n:
    if i.isdigit():
        s.append(int(i))
    if i == "+":
"""
def counter_add():
    k = int(input())

    def inner_func(cnt):
        return k + 5

    return inner_func



cnt = counter_add()
print(cnt)
