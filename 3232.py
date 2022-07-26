# (необязательная) Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно 
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# это олимпиадная задача.Первому игроку нужно смотреть, чтобы число конфет оставалось нечетным. 
# Тогда он сможет взять одну конфету и выиграть

import random

poisnenie = ('Вас приветствует игра - Забери конфеты!\n'
'Основные правила игры:\n'
'На столе лежит определенное количетсво конфет\n'
'Два игрока делают ходу поочереди\n'
'Первый ход определяется жеребьёвкой\n'
'За один ход можно забрать не более чем 28 конфет\n'
'Все конфеты оппонента достаются сделавшему последний ход\n'
'---------------------------------------------------------')
print(poisnenie)

def okonchanie(slovo):
    a = slovo % 10 # a - остаток от деления, number - число
    if slovo > -1: 
        if (11 <= slovo <= 14): return '' 
        elif (a == 0): return '' 
        elif (a == 1): return 'а'
        elif 2 <= a <= 4: return 'ы'
        elif 5 <= a <= 9: return ''
    else: return 'ошибка предела допустимых значений'

# def get_kolichestvo():
#     while True:
#         try:
#             ounter1 = int(input("Введите номер комнаты: "))
#             if counter > 0 and counter1 < 28 : " Введите число от 1 до 28"
#             return num
#         except ValueError:
#             print("Вы ввели не число. Повторите ввод")
# room_number = get_room_number()
# print(f"Комната {room_number} успешно забронирована!")

import random

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']

def reshenie(konfi, max_konfi, players, messages):
    # player1 = input('Давайте знакомиться, введите своё имя первый игрок\n')
    # player2 = input('Введите своё имя второй игрок\n')
 
    # konfet = int(input(f'Введите общее количество конфет\n'))
    # name = random.randint(0,1) # 1 и 0 это True = 1 и False = 0
    print(f' По правилу жеребьевки')
    count = 0
    count = random.choice([2, 1])
    print( count)
    if count == 2:
       print(f"Первый ходит {player1}") 
    else: 
        print(f"Первый ходит {player2}")

    # if name: # означает истинно, а значит True = 1
    #     print(f"Первый ходит {player1}")
    # else: # это лож, а False = 0
    #     print(f"Первый ходит {player2}")

    counter1 = 0
    counter2 = 0
    cold = 1 # раунды
    scet = 0 # за счет этого переключаю игроков

    if konfi % 10 == 1 and 9 > konfi % 10 > 10: letter = 'а'
    elif konfi % 10 == 0 and 9 > konfi % 10 > 10:letter = ''
    elif 2 <= konfi % 10 <= 4 and 9 > konfi % 10 > 10: letter = 'ы'
    else: letter = ''
    print(f' Раунд {cold}')
    print('------------------------')
    while konfi > 0 :  
        if scet % 2 == 0:
            print(f'{players[count % 1]}, {random.choice(messages)} ')   # count % 2= 0 это значит что ходит всего 1 игрок
            berem_konfi = int(input()) # вписываем число берем конфеты   
        elif scet % 2 != 0 :
            print(f'{players[count % 2]}, {random.choice(messages)} ')
            berem_konfi = int(input()) # вписываем число берем конфеты
     
        if berem_konfi > konfi or berem_konfi > max_konfi:  
            print(f'вы взяли очень много, не более {max_konfi} конфет{letter}' )
            attempt = 2
            while attempt > 0:
                if konfi >= berem_konfi <= max_konfi:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                berem_konfi = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток')
        konfi = konfi - berem_konfi
        if konfi > 0: 
            print(f'Осталось {konfi} конфет{okonchanie(konfi)}')
        else: print('Все конфеты разобраны.')
        cold += 1 # раунды 
        print(f' Раунд {cold}')
        print('------------------------')
        if konfi <= max_konfi: 
            if count == 2: print(f'Остается всего {konfi} {okonchanie(konfi)}, Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
            if count == 1: print(f'Остается всего {konfi} {okonchanie(konfi)}, Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')
        count +=1
        scet +=1
        print(scet)
       
          
   

player1 = 'Дмитрий'
player2 = 'Борис'  
players = [player1, player2]
konfi = 100
max_konfi = 28
winer = reshenie(konfi, max_konfi, players, messages)
print(winer)


            # if name: # и здесь так же пользуемся, потому что не за что привязать больше count
            #     # count = 1
            #     # counter1 = random.randint(1,28)               
            #     print(f'{player1}, вы забирали {counter1} конфет') 
            #     # print(f'Ваш ход {player1}, вы забирали {counter1} конфет') 
            #     konfi -= counter1 
            #     name = False # дает возможность переключать игроков в подобных условиях
            # else:      
            #     # counter2 = random.randint(1,28)
            #     # count = 0
            #     print(f'Ваш ход {player2}, вы забирали {counter2} конфет') 
            #     konfi-= counter2
            #     name = True # дает возможность переключать игроков в подобных условиях
            #     print(f'Осталось конфет', konfi)
            #     cold += 1 # раунды 
            #     print(f' Раунд {cold}')
            #     print('------------------------')




# gamer = (gamer % 2) + 1    это функция остатка от деления или же mod, в python она реализована как %, 
# то есть я беру остаток от деления на 2, для 1 это 2, для 2 это 0, то есть если я получаю 1 и плюсую 1, 
# 1 меняется на 2, а если было 2, я получу 0 и прибавлю 1 









# def okonchanie(slovo):
#     a = slovo % 10 # a - остаток от деления, number - число
#     if slovo > -1: 
#         if (11 <= slovo <= 14): return 'конфет' 
#         elif (a == 0): return 'конфет' 
#         elif (a == 1): return 'конфета'
#         elif 2 <= a <= 4: return 'конфеnы'
#         elif 5 <= a <= 9: return 'конфет'
#     else: return 'ошибка предела допустимых значений'


# # player1 = input('Давайте знакомиться, введите своё имя первый игрок\n')
# # player2 = input('Введите своё имя второй игрок\n')
# # player1 = 'Дмитрий'
# # player2 = 'Борис'  

# import random

# def reshenie():
#     player1 = 'Дмитрий'
#     player2 = 'Борис'  
#     name = random.randint(0,1) # 1 и 0 это True = 1 и False = 0
#     print(name)
#     if name: # означает истинно, а значит True = 1
#         print(f"Первый ходит {player1}")
#     else: # это лож, а False = 0
#         print(f"Второй ходит {player2}")
#     count = 0
#     konfet = 100
#     counter1 = 0
#     counter2 = 0
#     while konfet > 0 and konfet > 28: 
#             if name: # и здесь так же пользуемся, потому что не за что привязать больше count
#                 count = 1
#                 counter1 = random.randint(1,28) 
#                 print(f'Ваш ход {player1}, вы забирали {counter1} конфет') 
#                 konfet -= counter1 
#                 name = False # дает возможность переключать игроков в подобных условиях
#             else:      
#                 counter2 = random.randint(1,28)
#                 count = 0
#                 print(f'Ваш ход {player2}, вы забирали {counter2} конфет') 
#                 konfet -= counter2
#                 name = True # дает возможность переключать игроков в подобных условиях
#                 print(f'Осталось конфет', konfet)
#     if konfet <= 28: 
#         if count == 0: print(f'Остается всего {konfet} {okonchanie(konfet)}, Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
#         if count == 1: print(f'Остается всего {konfet} {okonchanie(konfet)}, Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')
#     return konfet
# reshenie()



# # gamer = (gamer % 2) + 1    это функция остатка от деления или же mod, в python она реализована как %, 
# # то есть я беру остаток от деления на 2, для 1 это 2, для 2 это 0, то есть если я получаю 1 и плюсую 1, 
# # 1 меняется на 2, а если было 2, я получу 0 и прибавлю 1 