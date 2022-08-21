from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

bot = telebot.Telebot('5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')

@bot.message_handler(commands= ['start'])

def start(message): # то что мы получим от подьзователя помещается в параметр (message)
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode= ' html ')

# запускаем бот на постоянное выполнение

bot.pollin(none_stop=True)