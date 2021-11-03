'''
tp = input().strip()
def get_sq(a, b=None):

    if b is None:
        return 2 * (a + b)
    else:
        return a * a


if tp == "RECT":
    get_sq(a, b)

else:
    get_sq(a)
'''
"""
n = eval(input())
"""
"""
n = list(map(str, input().split()))
count = 0

while len(n) != count:
    if len(n[count]) < 5:
        print("НЕТ")
    else:
        count += 1
    print("ДА")


"""
"""
def  get_rect_value(a, b, type=0):
    if type == 0:
        p = (a**2 - b**2)**0.5
        return  a + b + p
    else:
        p = (a + b + type) / 2
        return (p*(p-a)*(p-b)*(p-type))**0.5


print(get_rect_value(8, 4, 3))
"""

def check_password(password, chars="$%!?@#"):
    t = 0
    for i in password:
        if i in chars:
            t += 1
    if t >= 1 and len(password) >= 8:
        return True
    return False

print(check_password('12345678!'))



