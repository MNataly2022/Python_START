from telegram import Update
from telegram.ext import (
    ContextTypes,
)
from tabulate import tabulate
import model


async def printRecords(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Печать справочника'''

    await update.message.reply_text(tabulate(model.database, headers=model.properties, tablefmt="simple", maxcolwidths=[None, 8]))
    

async def inputRecordData(lst, update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Ввод данных строки справочника'''

    record = {}
    ind = 0
    for key in model.properties.keys():
        if key != 'id' and ind < len(lst):
            record[key] = lst[ind]
            ind += 1
    return record

    
async def printRecordData(record, update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Вывод данных строки справочника'''

    await update.message.reply_text('\n')
    for key in model.properties.keys():
        await update.message.reply_text(f'  {model.properties.get(key)}: {record[key]}')
    await update.message.reply_text('\n')
