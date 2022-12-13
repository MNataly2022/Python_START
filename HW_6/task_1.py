"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.
Ввод: значение типа <str>. Вывод: значение числового типа данных
"""
def calk(pstr):
    if "-" in  pstr:
        part_1, part_2 = pstr.split("-", 1)
        result = float(calk(part_1)) - float(calk(part_2)) 
    elif "+" in  pstr:
        part_1, part_2 = pstr.split("+", 1)
        result = float(calk(part_1)) + float(calk(part_2))
    elif "*" in  pstr:
        part_1, part_2 = pstr.split("*", 1)
        result = float(calk(part_1)) * float(calk(part_2))
    elif "/" in  pstr:
        part_1, part_2 = pstr.split("/", 1)
        result = float(calk(part_1)) / float(calk(part_2))
    else:
        result = float(pstr)
    return result 

string = input("Введите арифметическое выражение:  ")
string = ''.join(string.split())
while "(" in string:
    ss = string.split('(', 1)[1].split(')')[0]
    string = string.replace('(' + ss +')', str(calk(ss)))
print(f'{string} = {calk(string)}')