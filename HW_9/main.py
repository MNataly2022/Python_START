from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import const

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = 'I am Nataly Bot. I can \n '
    msg = msg + 'To convert number into binary code. You should enter "/double and your number" \n '
    msg = msg + 'For getting fibonacci numbers you should enter "/fib and your number" \n '
    msg = msg + 'For RLE-encryption you should enter "/rle and your number" \n '
    await update.message.reply_text(f'Hello {update.effective_user.first_name}.\n '+ msg)

def dec_to_bin(x):
    if x == 1:
        return 1

    return f'{dec_to_bin(x // 2)}{x % 2}'

async def double(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num = int(context.args[0])
    res = dec_to_bin(num)
    await update.message.reply_text(f'Number "{num}" in double is "{res}".')

def calc_fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

async def fibonacci(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num = int(context.args[0])
    res = list(calc_fibonacci(num))
    await update.message.reply_text(f'Fibonacci series for number "{num}" is "{res}".')

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

async def rle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lstr = update.message.text.split('rle ', 1)[1] #''.join(context.args) 
    res = RLE_coding(lstr)
    await update.message.reply_text(f'String "{lstr}" after RLE coding is "{res}".')



app = ApplicationBuilder().token(const.token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("double", double))
app.add_handler(CommandHandler("fib", fibonacci))
app.add_handler(CommandHandler("rle", rle_code))

app.run_polling()
