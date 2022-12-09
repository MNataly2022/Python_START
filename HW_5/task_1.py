"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».
Ввод: значение типа <str> Вывод: значение типа <str>

"""
# ВАриант 1 (мой)

text = 'Абревиатура букварь новый год весна надежда '
words = text.split(' ')
new_words = []

for word in words:
    if not ('а' in word.lower() and 'б' in word.lower()  and 'в' in word.lower()):
        new_words.append(word)
new_text = ' '.join(new_words)
print(new_text)

# Вариант 2

text = 'Абревиатура букварь новый год весна надежда. '
words = 'абв'
def del_words(txt, sym):
    return " ".join(filter(lambda x: not ("а" in x and "б" in x and "в" in x), txt.split()))  
print(del_words(text, words))

# Вариант 3

text = 'Абревиатура букварь новый год весна надежда. '
words = 'абв'
def del_words(txt, sym):
    return " ".join(filter(lambda x: not all(("а" in x, "б" in x, "в" in x)), txt.split()))  
print(del_words(text, words))

# Вариант 4

text = 'Абревиатура букварь новый год весна надежда. '
words = 'абв'
def del_words(txt, sym):
    return " ".join(filter(lambda x: not set(x) >=set (words), txt.split()))  
print(del_words(text, words))