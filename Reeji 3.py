from traceback import print_tb

a = int(input('Введите 1-ю сторону треугольника '))
b = int(input('Введите 2-ю сторону треугольника '))
c = int(input('Введите 3-ю сторону треугольника '))
if (a + b) > c:
    print('существует')
elif (a + c) > b:
    print('существует')
elif (b + c) > a:
    print('существует')
else:
    print('не существует')

if (a == b) and (a == c) and (c == b) :
    print('равносторонний')
elif (a == b) and (a == c) or (b == c) :
    print('равнобедренный')
elif (a != b) and (a != c) and (c != b):
    print('разносторонний')
else:
    print('неизвестный треугольник')