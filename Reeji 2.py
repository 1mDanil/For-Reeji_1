a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
math_ops =  input('Выберите математическую операцию: +, -, *, /, //, %, ** ')
if math_ops == '+':
    print(int(a + b))
elif math_ops == '-':
    print(int(a - b))
elif math_ops == '*':
    print(int(a * b))
elif math_ops == '/':
    print(int(a / b))
elif math_ops == '//':
    print(int(a // b))
elif math_ops == '%':
    print(int(a % b))
elif math_ops == '**':
    print(int(a ** b))
else:
    print('такой операции не существует')