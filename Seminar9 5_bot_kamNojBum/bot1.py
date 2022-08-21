import telebot 
import random

from telebot import types #keyboard module

TOKEN = '5575535064:AAHu_c7W5YhW5fd8rqjvHVy8osj3PiajeSU' # наш бот
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) # реагирует на команду старт, включается программа

def game_start(message): # создаем кнопки клавеатура
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton('Камень🤜')
	btn2 = types.KeyboardButton('Ножницы✌️')
	btn3 = types.KeyboardButton('Бумага✋')
	keyboard.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋ Выберите жест: ',\
		 reply_markup=keyboard)
@bot.message_handler(content_types=['text'])

def game(message): # сама программа
	computer = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
	if message.text == computer: # если выбор пользователя совпал с тем что быбрал компьютер то ничья
		bot.send_message(message.chat.id, 'Боевая ничья! Для начала новой игры пишите /start')

	else:
		if message.text == 'Камень🤜':
			if computer == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня {}. \
					Для начала новой игры пишите /start'.format(computer))
		elif message.text == 'Ножницы✌️':
			if computer == 'Бумага✋':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня {}.\
					 Для начала новой игры пишите /start'.format(computer))
		elif message.text == 'Бумага✋':
			if computer == 'Камень🤜':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня {}. \
					Для начала новой игры пишите /start'.format(computer))
			else:
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня {}. \
					Для начала новой игры пишите /start'.format(computer))
				
bot.polling(none_stop=True)
