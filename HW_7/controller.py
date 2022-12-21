import view
from logger import log
import model


@log
def start():
    """Стартовая функция"""
    view.greatings()
    model.load()
    while True:
        view.separator()
        match view.chooseMenu():
            case '1':  # Посмотреть справочник
                view.separator()
                view.printRecords(model.database)
            case '2':  # Добавить строку в справочник
                view.separator()
                newRecord = view.inputRecordData()
                model.add_record(newRecord)
            case '3':  # Редактировать строку справочника
                view.separator()
                recordNum = view.inputRecordNumber()
                record = model.get_record(recordNum)
                if record != []:
                    view.printRecordData(record)
                    newRecord = view.inputRecordData()
                    model.edit_record(recordNum, newRecord)
                else: 
                    view.error('Строка не найдена !')
            case '4':  # Удалить строку справочника
                view.separator()
                recordNum = view.inputRecordNumber()
                model.delete_record(recordNum)
            case '5':  # Закончить работу
                break 
            case _:
                view.error()
    #model.save()
    view.separator()
    view.bay()
