from logger import log

@log
def greatings():
    '''Вывод приветствия'''

    print('Я телефонный справочник.')

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

    print(f'ID\tИмя\t\tФамилия\t\tДата рождения\tМесто работы\t\t\tНомер телефона')
    print(f'______  ______________  ______________  ______________  ______________________________  ____________________________')
    lenCol = 16
    for item in data: 
        print(f'{" "*2}{item["id"]}\t{item["first name"]}{" "*(lenCol-len(item["first name"]))}{item["surname"]}{" "*(lenCol-len(item["surname"]))}{item["birth day"]}{" "*(lenCol-len(item["birth day"]))}{item["job"]}{" "*(lenCol*2-len(item["job"]))}{item["phone"]}')
    
    
@log
def inputRecordData():
    '''Ввод данных строки справочника'''

    print('Введите данные строки: ')
    record = {}
    record['first name'] = input('  Имя: ')
    record['surname'] = input(' Фамилия: ')
    record['birth day'] = input(' Дата рождения: ')
    record['job'] = input(' Место работы: ')
    record['phone'] = input(' Номер телефона: ')
    return record

    
@log
def printRecordData(record):
    '''Вывод данных строки справочника'''

    print('\n')
    print(f'ID: {record["id"]}')
    print(f'Имя: {record["first name"]}')
    print(f'Фамилия: {record["surname"]}')
    print(f'Дата рождения: {record["birth day"]}')
    print(f'Место работы: {record["job"]}')
    print(f'Номер телефона: {record["phone"]}')
    print('\n')

