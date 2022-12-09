"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на
один символ и число его повторов. На первом месте идет количество повторов, на втором
сам символ. Восстановите строку после шифрования. Ввод: значения типа <str>, можно 
получить из файла. Вывод: значение типа <str>, можно записать в файл.
Примеры: ыыыыыррррр   аааааагггггггг 5ы5р3 6а8г
"""
data = input("Введите строку символов ")

def RLE_coding(data):
    code = ''
    previous_symbol = ''
    count = 1

    if not data:
        return ''

    for current_symbol in data:
        if current_symbol !=  previous_symbol:
            if previous_symbol:
                code += str(count) + previous_symbol
            count = 1
            previous_symbol = current_symbol
        else:
            if count == 9:
                code += str(count) + previous_symbol
                count = 1
            count += 1
    code += str(count) + previous_symbol
    return(code)
code = RLE_coding(data)
print(code)

def RLE_decoding(data):
    decode = ''
    for i in range(0, len(data),2):
        count, symbol = data[i: i + 2]      
        decode += symbol * int(count)
    return decode
print(RLE_decoding(code))
