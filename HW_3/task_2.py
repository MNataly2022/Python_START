"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>
Пример:[2, 3, 4, 5, 6] / [12, 15, 16],  [2, 3, 5, 6] / [12, 15]
"""
import random
n = int(input("ВВедите число N "))
my_list = [random.randint(0, n) for i in range(n)]
print(my_list)

new_list = []
for i in range(0, (n + 1) // 2):
    new_list.append(my_list[i] * my_list[- i - 1])
print(new_list)