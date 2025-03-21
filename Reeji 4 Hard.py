import math
a = int(input('Введите a коэффицент '))
b = int(input('Введите b коэффицент '))
c = int(input('Введите c коэффицент '))
if a == 0 and b == 0 and c == 0:
    print('Уравнение будет равно 0')
elif b == 0:
    g = c / a
    x1 = math.sqrt(g)
    x2 = -math.sqrt(g)
    print(x1, x2)
elif c == 0:
    x1 = 0
    x2 = b % a
    print(x1, x2)
elif b == 0 and c == 0:
    x = 0
    print(x)
elif a == 0:
    x = c % b
    print(x)
elif a == 0 and b == 0:
    print('Корней нет')
elif a == 0 and c == 0:
    print(int(0))
elif a != 0 and b != 0 and c != 0:
    disc = b * b - 4 * a * c
    if disc < 0:
        print('корней нет')
    elif disc == 0:
        x = -b/(2 * a)
        print(x)
    elif disc > 0:
        x1 = -b - math.sqrt(disc) /(2 * a)
        x2 = -b + math.sqrt(disc) /(2 * a)
    print(x1, x2)
else:
    print('ya zaputalsya')


