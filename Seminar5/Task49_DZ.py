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

import random

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
                x = int(input(f"{name}, введите корректное количество конфет: "))       
    return x

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']

def reshenie():
    # player1 = input('Давайте знакомиться, введите своё имя первый игрок\n')
    # player2 = input('Введите своё имя второй игрок\n')
    konfi = int(input(f'Введите общее количество конфет\n'))
    print(f' По правилу жеребьевки')
    player1 = 'Дмитрий'
    player2 = 'Борис'  
    # konfi = 100
    max_konfi = 28
    name = random.choice([0, 1])
    # print( count)
    if name:
       print(f"Первый ходит {player1}") 
    else: 
        print(f"Первый ходит {player2}")
    print('------------------------')
    if konfi % 10 == 1 and 9 > konfi > 10: letter = ''
    elif 1 < konfi % 10 < 5 and 9 > konfi > 10: letter = 'ы'
    else: letter = ''
    while konfi > 0 and konfi > max_konfi:   
        if name:     
            berem_konfi = input_dat(player1) # вписываем число берем конфеты    
            konfi = konfi - berem_konfi    
            name = False
            print(f'{player1}, {random.choice(messages)}') 
            print(f'Дмитрий взял {berem_konfi} конфет{letter}')
        else:   
            berem_konfi = input_dat(player2) # вписываем число берем конфеты
            konfi = konfi - berem_konfi  
            name = True
            print(f'{player2}, {random.choice(messages)}')
            print(f'Ботрис взял {berem_konfi} конфет{letter}')
        print(f'Осталось {konfi} конфет{okonchanie(konfi)}')         
         # print(scet)
        print('------------------------------')   
    if name: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
    else: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')      
    return konfi      

def reshenie2():
    # konfi = int(input(f'Введите общее количество конфет\n'))
    print(f' По правилу жеребьевки')
    player1 = 'Дмитрий'
    player2 = 'Борис'  
    konfi = 100
    max_konfi = 28
    name = random.choice([0, 1])
    # print( count)
    if name:
       print(f"Первый ходит {player1}") 
    else: 
        print(f"Первый ходит {player2}")
    print('------------------------')
    if konfi % 10 == 1 and 9 > konfi > 10: letter = ''
    elif 1 < konfi % 10 < 5 and 9 > konfi > 10: letter = 'ы'
    else: letter = ''
    while konfi > 0 and konfi > max_konfi:   
        if name:  
            berem_konfi = input_dat(player1) # вписываем число берем конфеты    
            konfi = konfi - berem_konfi    
            print(f'{player1}, {random.choice(messages)}')  
            print(f'Дмитрий взял {berem_konfi} конфет{letter}')
            name = False
        else:   
            berem_konfi = random.randint(1,28) # вписываем число берем конфеты
            konfi = konfi - berem_konfi  
            name = True
            print(f'{player2}, {random.choice(messages)}')
            print(f'Борис взял {berem_konfi} конфет{letter}')
        print(f'Осталось {konfi} конфет{okonchanie(konfi)}')         
         # print(scet)
        print('------------------------------')   
    if name: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
    else: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')      
    return konfi 

def reshenie3():
    # konfi = int(input(f'Введите общее количество конфет\n'))
    print(f' По правилу жеребьевки')
    player1 = 'Дмитрий'
    player2 = 'Борис'  
    konfi = 100
    x = 1
    y = 2
    max_konfi = 28
    name = random.choice([0, 1])
    # print( count)
    if name:
       print(f"Первый ходит {player1}") 
    else: 
        print(f"Первый ходит {player2}")
    print('------------------------')
    if konfi % 10 == 1 and 9 > konfi > 10: letter = ''
    elif 1 < konfi % 10 < 5 and 9 > konfi > 10: letter = 'ы'
    else: letter = ''
    while konfi > 0 and konfi > max_konfi:   
        if name:  
            berem_konfi = input_dat(player1) # вписываем число берем конфеты    
            konfi = konfi - berem_konfi    
            print(f'{player1}, {random.choice(messages)}')  
            print(f'Дмитрий взял {berem_konfi} конфет{letter}')
            name = False
        else:  
            if konfi % 2 == 0:
                berem_konfi = x 
            else:
                berem_konfi = y
            konfi = konfi - berem_konfi  
            name = True
            print(f'{player2}, {random.choice(messages)}')
            print(f'Борис взял {berem_konfi} конфет{letter}')
        print(f'Осталось {konfi} конфет{okonchanie(konfi)}')         
         # print(scet)
        print('------------------------------')   
    if name: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
    else: print(f'Остается всего {konfi} конфет{okonchanie(konfi)}, Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')      
    return konfi 

def game():
    while True:
        try:
            x = int(input('Выберите игру с (1)человеком (2)компьютером или (3)суперкомпьютером\n'))
            while x <= 0 or x > 3:
                x = int(input('Введите корректное число')   ) 
        except ValueError: print("Вы ввели не число. Повторите ввод")
        else:
            if x == 1: 
                print('игра с человеком')
                return reshenie() 
            elif x == 2: 
                print('игра с компьютером')
                return reshenie2()
            elif x == 3:
                print('игра с суперкомпьютером')
                return reshenie3()
game()

# gamer = (gamer % 2) + 1    это функция остатка от деления или же mod, в python она реализована как %, 
# то есть я беру остаток от деления на 2, для 1 это 2, для 2 это 0, то есть если я получаю 1 и плюсую 1, 
# 1 меняется на 2, а если было 2, я получу 0 и прибавлю 1 