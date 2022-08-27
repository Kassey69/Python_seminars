import telebot 
import random

from telebot import types #keyboard module

#  все о командах ботов -            https://habr.com/ru/sandbox/149884/

# CommandHandler - реагирует на команды print и input меняем на это
# MessageHandler - реагирует на сообщения
# Взаимодействие с ботом происходит через переменную bot (токен надо вставить свой). 
# Декоратор @message_handler реагирует на входящие сообщение. 
# Message – это объект из Bot API, содержащий в себе информацию о сообщении. 
# Полезные поля: message.chat.id – идентификатор чата 
# message.from.id – идентификатор пользователя 
# message.text – текст сообщения 
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.

TOKEN = '5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU' # наш бот
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) # запускаем бот

def game_start(message): # создаем клавеатуру кнопки для нажатия

	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton('Камень🤜')
	btn2 = types.KeyboardButton('Ножницы✌️')
	btn3 = types.KeyboardButton('Бумага✋')
	keyboard.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋ Выберите жест: ',\
		 reply_markup=keyboard)

@bot.message_handler(content_types=['text']) # основной код программы

def game(message):
	computer = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
	if message.text == computer:
		
		bot.send_message(message.chat.id, 'Боевая ничья! Для начала новой игры пишите /start')

	else:
		if message.text == 'Камень🤜':
			if computer == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. \
					Для начала новой игры пишите /start'.format(computer))
		elif message.text == 'Ножницы✌️':
			if computer == 'Бумага✋':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}.\
					 Для начала новой игры пишите /start'.format(computer))
		elif message.text == 'Бумага✋':
			if computer == 'Камень🤜':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. \
					Для начала новой игры пишите /start'.format(computer))
			
	
	
bot.polling(none_stop=True)



# Замена клавиатуры
# У ботов есть функция замены стандартной клавиатуры на кнопочную. 
# Для этого у всех функций есть опциональный аргумент reply_markup:

# from telebot import types

# @bot.message_handler(commands=['start'])
# def start(message):
#   markup = types.ReplyKeyboardMarkup()
#   buttonA = types.KeyboardButton('A')
#   buttonB = types.KeyboardButton('B')
#   buttonC = types.KeyboardButton('C')

#   markup.row(buttonA, buttonB)
#   markup.row(buttonC)

#   bot.send_message(message.chat.id, 'It works!', reply_markup=markup)

# ReplyKeyboardMarkup – и есть та самая клавиатура. 
# Метод row() создает ряд (максимум 12) из кнопок, передаваемых в качестве аргумента.
# Также есть особенная клавиатура types.ReplyMarkupRemove(), которая меняет клавиатуру на стандартную.



        
# Клавиатура для сообщений
# Можно создавать клавиатуру для отдельного сообщения. Передавать его нужно так же в аргумент reply_markup:

# from telebot import types

# @bot.message_handler(commands=['start'])
# def start(message):
#   markup = types.InlineKeyboardMarkup()
#   buttonA = types.InlineKeyboardButton('A', callback_data='a')
#   buttonB = types.InlineKeyboardButton('B', callback_data='b')
#   buttonC = types.InlineKeyboardButton('C', callback_data='c')

#   markup.row(buttonA, buttonB)
#   markup.row(buttonC)

#   bot.send_message(message.chat.id, 'It works!', reply_markup=markup)


# У кнопок есть несколько режимов, в зависимости от второго аргумента. 
# Подробнее можно прочитать в официальной документации, но я остановлюсь только на callback_data.
# При нажатии на такую кнопку боту придет отдельный CallbackQuery, 
# который нужно обрабатывать подобно сообщению:

# @bot.callback_query_handler(func=lambda call: True)
# def handle(call):
# 	bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))
#   bot.answer_callback_query(call.id)
# Для обработки обязательно указать аргумент func для "отсеивания" Callback запросов.
# После обработки каждого запроса нужно выполнить команду answer_callback_query, 
# чтобы Telegram понял, что запрос обработан. В поле callback.data 
# хранится информация из callback_data нажатой кнопки.