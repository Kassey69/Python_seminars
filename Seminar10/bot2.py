import telebot 
import random

from telebot import types #keyboard module

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

@bot.message_handler(content_types=['text']) 

def game(message): # основной код программы
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

        
