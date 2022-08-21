# Задание создать новый хендлер , бот должен рассказывать при вызове о создателе
import igrs_ksmen as i_k
# igra()
from turtle import update
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters,ConversationHandler

bot = Bot(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')
updater = Updater(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU', use_context=True)
dispatcher = updater.dispatcher

'''Все  что выше стандарт , меняесть токен и библиотеки'''

START = 0
BIO = 1
PHOTO = 2

def start(update, context):
    context.bot.send_message(update.effective_chat.id, ' Введите мнимую часть ')
    return START

def input_data_1(update, context):
    global first_number
    first_number = update.message.text
    print(first_number)
    context.bot.send_message(update.effective_chat.id, ' Введите действенную часть ')
    return BIO

def input_data_2(update, context):
    global second_number
    second_number = update.message.text
    print(second_number)
    context.bot.send_message(update.effective_chat.id, ' Введите действие ')
    return PHOTO

def photo(update, context):
    text = update.message.text
    if text == '+':
        context.bot.send_message(update.effective_chat.id, f' {int(first_number) + int(second_number)} ')

def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, input_data_1)
second_handler = MessageHandler(Filters.text, input_data_2)
cancel_handler = CommandHandler('cancel', cancel)
photo_handler = MessageHandler(Filters.text, photo)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={START: [first_handler], 
                                            BIO: [second_handler],
                                            PHOTO: [photo_handler]},
                                    fallbacks = [cancel_handler ])   


dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()






