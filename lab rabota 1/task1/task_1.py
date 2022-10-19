list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
list_unique = (set(list_))
print(sum(list_unique))
print(len(list_unique))
print(round(sum(list_unique)/len(list_unique), 5))