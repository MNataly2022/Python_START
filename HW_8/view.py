from logger import log
import model
from tabulate import tabulate 

@log
def greatings():
    '''Вывод приветствия'''

    print('Я справочник учеников школы.')

@log
def bay():
    '''Вывод прощания'''

    print('До свидания.')

@log
def separator():
    '''Вывод разделителя'''

    print("."*120)

@log
def error(msg = ""):
    '''Вывод сообщения о ошибке'''

    print(f'Ошибка. {msg}')

@log
def chooseMenu():
    '''Работа меню'''

    return input('Что Вы хотите сделать: \n'
                '   1. Посмотреть справочник \n'
                '   2. Добавить строку в справочник \n'
                '   3. Редактировать строку справочника \n'
                '   4. Удалить строку справочника \n'
                '   5. Закончить работу \n'
                'Для выбора введите номер пункта: ')

@log
def inputRecordNumber():
    '''Ввод номера строки справочника'''

    return int(input('Введите номер строки справочника: '))

@log
def printRecords(data):
    '''Печать справочника'''
  
    print(tabulate(data, headers=model.properties, tablefmt="grid"))
    
@log
def inputRecordData():
    '''Ввод данных строки справочника'''

    print('Введите данные строки: ')
    record = {}
    for key in model.properties.keys():
        if key != 'id':
            record[key] = input(f'  {model.properties.get(key)}: ')
    return record

    
@log
def printRecordData(record):
    '''Вывод данных строки справочника'''

    print('\n')
    for key in model.properties.keys():
        print(f'  {model.properties.get(key)}: {record[key]}')
    print('\n')

