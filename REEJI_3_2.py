kortej = (1, 2, 3, 4, 5, 6, 7, 8)

chetnie = tuple(x for x in kortej if x % 2 == 0)
nechetnie = tuple(x for x in kortej if x % 2 != 0)

print(f"Чётные числа {chetnie}")
print(f'Нечётные числа {nechetnie}')