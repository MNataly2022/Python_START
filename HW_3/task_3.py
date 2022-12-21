"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>
Пример: [1.1, 1.2, 3.1, 5, 10.01] // 2.0
"""
import random
n = int(input("ВВедите число N "))
my_list = [round(random.random() * n, 2) for i in range(n)]
print(my_list)

new_list = []
for i in range(0,n):
    new_list.append(int(my_list[i] * 100 % 100))
print(new_list)

max = 0 
for i in range(0,n):
   if new_list[i] > max:
      max = new_list[i]

min = new_list[0]      
for i in range(0,n):
   if new_list[i] < min:
       min = new_list[i]       
print(float((max - min) / 100))