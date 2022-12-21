"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt 
(в одной строке один индекс). Решение должно работать при любом натуральном N.
Ввод: значение типа <int> Вывод: значение типа <int>
"""

import random
n = int(input("Введите число: "))
my_list = [random.randint(-n, n) for r in range(n)]

index_list = []
prod = 1

with open('indexes.txt', 'r') as file:
    for index in file:
        index_list.append(int(index))
for i in range(-n, n):
    if i in index_list:
        prod *= my_list[i]
print(prod)       