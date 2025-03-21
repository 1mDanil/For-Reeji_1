temperature = int(input('Введите температуру в ЦЕЛЬСИЯХ!!!'))
convert = input('В какую еденицу измерения конвертировать? F или K ')
if convert == 'F':
    print((temperature * 9/5) + 32)
elif convert == 'K':
    print(temperature + 273.15)
else:
    print('Введена неверная еденица измерения')