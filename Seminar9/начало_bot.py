from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# bot_token = '5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU' # сдесь идет привязка бота, вписываем токен
# bot = Bot(token=bot_token)
#  более коротко бцдет так 
bot = Bot(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')

# Updater - позволяет получать все обновления от пользователя, он отлавливает их анализирует 
# dispatcher - помощник бота
# handlerHandler - самая важная часть бота, это обработчик событий , событие это получение сообщения от пользователя


updater = Updater(token='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU', use_context=True)
dispatcher = updater.dispatcher



# handlerHandler - это обычная функця в питоне, мы создаем ее и называем к примеру start
# далее он принимает 2 важных аргумента (update, context)
# c помощтю update мы узгаем из какого id , номер чатаЮ, имя пользователя, само сообщение, время отправки
# context - аргумент который понимает только телеграмм сервер



'''Все  что выше стандарт , меняесть токен и библиотеки'''

def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                                " привет! для поиска информации в wiki отправь команду \n/find запрос ")

# мы с помощью context с мопощью бота context.bot. 
# отправляем сообщение context.bot.send_message в update.effective_chat.id, потому что у кажддого чата
# есть свой уникальный идентификатор
# а далее мы передаем сообщение которое мы будем отправлять
                             #   " привет! для поиска информации в wiki отправь команду \n/find запрос ")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# CommandHandler - позволдяет наам создать связку и указываем что нам должен писать пользователь CommandHandler('start',
# если пользователь напишет 'start то мы вызываем команду start - CommandHandler('start', start)
# там может написано быть а CommandHandler('а', start) все равно вызовем команду start)

# в чем смысл диспетчера - dispatcher.add_handler(start_handler)
# диспетчер это своего рода список, в котором мы добавляем команды нашего бота, возможности бота
# если мы не добавим dispatcher.add_handler(start_handler) то наш бот по сути ничего не сможет уметь  


updater.start_polling()
updater.idle()

# эти функции updater.start_polling() ,  updater.idle() заставляют нашего бота принимать сообщения
#  эти функции всегда пишутся в конце, они помогают боту работать, позволяют принимать ссообщенияы



