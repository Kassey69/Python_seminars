
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters # включение на бота

# CommandHandler - реагирует на команды
# MessageHandler - реагирует на сообщения

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    else:
        try:
            update.message.reply_text(eval(update.message.text)) # считает математику
        except:
            update.message.reply_text("Не понятно")

updater = Updater('5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU') # создаем телеграмм бот 

updater.dispatcher.add_handler(CommandHandler('hello', hello)) # добавляем функции в функционал бота
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))
print('server start')
updater.start_polling()
updater.idle()






        
