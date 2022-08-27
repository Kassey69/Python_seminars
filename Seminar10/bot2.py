# Use this token to access the HTTP API:
# 5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU

# CommandHandler - реагимрует на команды print и input меняем на это
# MessageHandler - реагирует на сообщения
# все о создании кнопок ботов и прочем https://habr.com/ru/post/580408/ 

import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

updater = Updater('5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'К работе готов')

users = {'Алешка': '7777755', 'Мишка':'3344343', 'Маис': '34234234' } # создали словарь

def dict(update: Update, context: CallbackContext): # обработка сообщений
	if (update.message.text in users ): # если ключ есть в users то мы выводим его значение
			update.message.reply_text(users[update.message.text]) # то мы выводим его значение


def save_1(update: Update, context: CallbackContext):
	with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar10\phonenumber.json',\
		'w', encoding='utf-8') as pN:
		pN.write(json.dumps(users, ensure_ascii=False))
	# print('успешно созранено')
	update.message.reply_text(f'успешно созранено')


def del_1(update: Update, context: CallbackContext):
	with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar10\phonenumber.json',\
		'r', encoding='utf-8') as pN:
		users = json.load(pN)
		del users['Алешка']
		update.message.reply_text(f'успешно удалено')
	with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar10\phonenumber.json',\
		 'w', encoding='utf-8') as pN:
      		json.dump(users, pN, ensure_ascii=False)		
# print('успешно удалено')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
# мы связываем какую то описанную выше функцию и мы сявязваем с каим то типом либо 
# обработки команды CommandHandler
# либо обработка сообщений MessageHandler

updater.dispatcher.add_handler(CommandHandler('save_1', save_1))
updater.dispatcher.add_handler(CommandHandler('del_1', del_1))
updater.dispatcher.add_handler(MessageHandler(Filters.text, dict))

print('server start')
updater.start_polling()
updater.idle()










# path = 'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar10\phonenumber.json'
# f = open(path, 'w')
# data = f.write() + ' '
# f.close()

# dict1 = {}





# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext


# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# updater = Updater('YOUR TOKEN HERE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# print('server start')
# updater.start_polling()
# updater.idle()