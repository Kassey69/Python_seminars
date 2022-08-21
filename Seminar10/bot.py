# Use this token to access the HTTP API:
# 5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


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

updater = Updater('5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))


print('server start')
updater.start_polling()
updater.idle()


# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext


# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# updater = Updater('YOUR TOKEN HERE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# print('server start')
# updater.start_polling()
# updater.idle()