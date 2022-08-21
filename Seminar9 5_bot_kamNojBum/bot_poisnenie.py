
# устанавливаем pip install pyTelegramBotApi
# импортируем 3 модуля: pyTelegramBotApi, random и модуль из pyTelegramBotApi под названиям types:
import telebot
import random
from telebot import types
# Модуль types из telebot нужен для клавиатуры бота (типо кнопок снизу поля для ввода сообщения).

TOKEN='5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU'
# Дальше нам обязательно надо добавить объект класса telebot.TeleBot и передать в качестве параметра наш токен:
bot = telebot.TeleBot(TOKEN)

# Нам также надо будет делать ответ на старт игры (на команду /start). 
# Для этого необходимо создать функцию с декоратором @bot.message_handler:
@bot.message_handler(commands=['start'])

# def game_start(message):
#     pass # на пока что

# И давайте вместо pass поставим "Камень, ножницы, бумага раз, два, три!":

# def game_start(message):
#     bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋, раз, два, три! Выберите жест:')

# Ну что ж, теперь нам надо создать "клаву":

def game_start(message):
# Build keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton('Камень🤜')
    btn2 = types.KeyboardButton('Ножницы✌️')
    btn3 = types.KeyboardButton('Бумага✋')
    keyboard.add(btn1, btn2, btn3) # Добавляем кнопки
    bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋, раз, два, три! Выберите жест:', \
         reply_markup=keyboard)

# Теперь давайте сделаем реакцию на нажатию кнопок. Для этого надо создать новую функцию с декоратором 
# @bot.message_handler, только с другими параметрами.

@bot.message_handler(content_types=['text'])
def game(message):
	choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
	if message.text == choice: # если вводимый мной текст равен тому что на рандом у компьютера
		bot.send_message(message.chat.id, 'Боевая ничья! Для начала новой игры пишите /start')
	else:
		if message.text == 'Камень🤜':
			if choice == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Поздравляю с победой! Для начала новой игры пишите /start')
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. Для начала новой игры пишите /start')
		elif message.text == 'Ножницы✌️':
			if choice == 'Бумага✋':
				bot.send_message(message.chat.id, 'Поздравляю с победой! Для начала новой игры пишите /start')
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. Для начала новой игры пишите /start')
		elif message.text == 'Бумага✋':
			if choice == 'Камень🤜':
				bot.send_message(message.chat.id, 'Поздравляю с победой! Для начала новой игры пишите /start')
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. Для начала новой игры пишите /start')
bot.polling(none_stop=True)
        
