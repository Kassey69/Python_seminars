# Задание создать новый хендлер , бот должен рассказывать при вызове о создателе

from turtle import update
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

bot = Bot(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')
updater = Updater(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU', use_context=True)
dispatcher = updater.dispatcher

'''Все  что выше стандарт , меняесть токен и библиотеки'''

def start(update, context):
    arg = context.args # передается весь список аргументов , context.args - список переданных аргументов
    print(arg)
    context.bot.send_message(update.effective_chat.id, f" {' '.join(arg)} ") # сейчас он будет дублировать ответ на 
    # ейчас он будет дублировать ответ на  def start
    # context.bot.send_message(update.effective_chat.id,
    #                             " привет! для поиска информации в wiki отправь команду \n/find запрос ")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, " создатель мой человек очень хороший, его все любят и он тоже")


def message(update, context):
    # pass # позволяет вызывыать функцию, но она ничего не будет возвращать, заглушка
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id,
                                " И тебе привет ")
    else:
        context.bot.send_message(update.effective_chat.id,
                                " Я тебя не понимаю ") # это для того чтобы на любые другие команды от писал 

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)
# в телеграмме самма команда это тоже текст и в этом подвох
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)  # его нужно добавлять в конце всех команд иначе будут они игнориться


# как указать что это текст , существует Filters , она ильтурет отправленные сообщения
# она определяет что это голосовое сообщение или видео или фото или текст


updater.start_polling()
updater.idle()






