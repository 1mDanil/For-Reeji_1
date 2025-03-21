name_surname = input('Введите ваше ФИО!')
age = int(input('Введите ваш год рождения!'))
county = input('Напишите страну в которой проживаете!')

human_age = int(2025 - age)

if human_age <= 18:
    print(name_surname, ', возраст состовляет ' + str(human_age), 'года, проживает в стране ' + county, ', несовершеннолетний')
elif human_age >= 18:
    print(name_surname, ', возраст состовляет ' + str(human_age), 'года, проживает в стране ' + county,', совершеннолетний')
else:
    print('Не существует такого года рождения')


