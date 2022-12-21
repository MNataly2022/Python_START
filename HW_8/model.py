from logger import log

import json
from os import path

database = []
properties = {'id': 'ID', 
    'first name': 'Имя',
    'surname': 'Фамилия',
    'birth day': 'Дата рождения',
    'phone': 'Номер телефона',
    'class': 'Класс' 
    }

@log
def load():
    """
    Загружает данные из файла и возвращает список словарей
    """
    global database
    if path.isfile("phone_db.json"):
        with open("phone_db.json", 'r', encoding="utf-8") as file:
            database = json.load(file)
    else:
        database = []


@log
def save():
    """
    Сохраняем данные в файл
    """
    
    with open("phone_db.json", "w", encoding="utf-8") as file:
        json.dump(database, file, indent=2, ensure_ascii=False)



@log
def get_record(num: int) -> dict:
    """
    Загружает данные из файла и возвращает словарь с индексом.
    :param num:
    """
    num = num - 1
    record = []
    if num >= 0 and num <= len(database)-1:
        record = database[num]
    return record    

   

@log
def add_record(data: dict):
    """
    Принимает словарь с записью и добавляет в файл..
    :param data:
    """
    global database
    id = len(database) + 1
    data["id"] = id
    database.append(data)
    save()

@log
def delete_record(num: int):
    """
    Удаляет строку справочника по индексу и записывает в файл..
    :param num: int
    """
    global database
    num = num -1
    if num >= 0 and num <= len(database)-1:
        database.remove(database[num])
        save()

@log
def edit_record(num: int, data: dict):
    """
    Принимает словарь с записью и заменяет словарь с индексом.
    :param num: int, data: dict 
    """
    global database
    num = num -1
    if num >= 0 and num <= len(database)-1:
        database[num].update(data)
        save()
