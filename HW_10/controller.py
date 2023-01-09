from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

import const
import view
import model
import task_4

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = 'I am Nataly Bot. I can \n '
    msg = msg + 'To show phone dict. You should enter "/show" \n '
    msg = msg + 'To add new item in phone dict. You should enter "/add ....;.....;" \n '
    msg = msg + 'To edit item from phone dict. You should enter "/edit num;....;.....;" \n '
    msg = msg + 'To delete item from phone dict. You should enter "/delete num" \n '
    msg = msg + 'To calc polynom sum. You should enter "/calc ....;.....;" \n '
    await update.message.reply_text(f'Hello {update.effective_user.first_name}.\n '+ msg)
    model.load()

async def show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await view.printRecords(update, context)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lstr = update.message.text.split('add ', 1)[1] #''.join(context.args) 
    item = lstr.split(';')
    ditem = await view.inputRecordData(item, update, context)
    model.add_record(ditem)
    await update.message.reply_text(f'Item [{lstr}] added.')

async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lstr = update.message.text.split('edit ', 1)[1] #''.join(context.args) 
    item = lstr.split(';')
    recordNum = int(item[0])
    record = model.get_record(recordNum)
    if record != []:
        await view.printRecordData(record, update, context)
        item.remove(item[0])
        newRecord = await view.inputRecordData(item, update, context)
        model.edit_record(recordNum, newRecord)
    else: 
        await update.message.reply_text(f'Строка не найдена !')

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    recordNum =  int(context.args[0])
    record = model.get_record(recordNum)
    if record != []:
        await view.printRecordData(record, update, context)
        model.delete_record(recordNum)
        await update.message.reply_text(f'Строка удалена !')
    else: 
        await update.message.reply_text(f'Строка не найдена !')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lstr = update.message.text.split('calc ', 1)[1] #''.join(context.args) 
    item = lstr.split(';')
    res_polynom = ""
    for polynom in item:
        res_polynom = task_4.sum_polynom(res_polynom, polynom)
    await update.message.reply_text(f'Polynom sum is {res_polynom}.')

def run():
    """Стартовая функция"""

    app = Application.builder().token(const.token).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("hi", hello))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("show", show))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("edit", edit))
    app.add_handler(CommandHandler("delete", delete))
    app.add_handler(CommandHandler("calc", calc))

    app.run_polling()
    
    """
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
    """