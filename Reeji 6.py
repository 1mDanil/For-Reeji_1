year = int(input('Введите год на проверку '))
def visyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 'Високосный'
            else:
                return 'Не високосный'
        else:
            return 'Високосный'
    else:
        return 'Не високосный'
    return year
print(visyear(year))
