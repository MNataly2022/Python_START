
""" Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений
Ввод: значение типа <list>.  Вывод: три объекта типа <list>
Пример: [1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
from random import randint

n = int(input("Введите натуральное число N "))
my_list = [randint(0,n) for i in range(n)]
print(my_list)
result_list1 = []
result_list2 = []
result_list3 = []
result_list4 = []

for number in my_list: 
    if my_list.count(number) == 1:
        result_list1.append(number) 
print(f'Список чисел, которые не повторяются:  {result_list1}')

for number in my_list: 
    if my_list.count(number) > 1:
        result_list2.append(number)
        if number not in result_list4:
            result_list4.append(number) 
print(f'Список чисел, которые повторяются:  {result_list4}')

for number in my_list:
    if number not in result_list3:
        result_list3.append(number) 
print(f'Список без повторений:  {result_list3}')