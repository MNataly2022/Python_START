"""
Задать натуральное число k. Сформируйте многочлен (полином) степени k со случайными коэффициентами
из промежутка от 0 до 100, включительно. Многочлен вывести в консоль и записать в файл.
Ввод: значение типа <int>. Вывод: значение типа <str>, файл с одной строкой.
Пример: 2  2x^2 + 4x + 5 = 0
"""

from random import randint
from os import path, mkdir, chdir


def create_polinom(list_k):
    if sum(list_k) == 0:
        return '0 = 0'

    i = len(list_k) - 1
    my_polynom = []
    for k in list_k:
        if k:
            if i == 0:
                my_polynom.append(f'{k}')
            elif i == 1:
                my_polynom.append(f'{k if k != 1 else ""}x')
            else:
                my_polynom.append(f'{k if k != 1 else ""}x^{i}')
        i -= 1
    return ' + '.join(my_polynom) + ' = 0'


if __name__ == '__main__':
    k = int(input("Введите степень полинома k "))
    coef = [randint(0, 100) for i in range(k)]
    result_polynom = create_polinom(coef)
    print(result_polynom)

    if not path.isdir("polynom"):
        mkdir("polynom")
    chdir("polynom")
    i = 0
    while True:
        if not path.isfile(f"polynom_{i}.txt"):
            with open(f"polynom_{i}.txt", 'w') as file:
                file.write(result_polynom)
            break
        else:
            i += 1
  