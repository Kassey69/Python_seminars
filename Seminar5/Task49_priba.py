from random import randint
import random

def reshenie2():
    player1 = 'Дмитрий'
    player2 = 'Борис'  
    name = random.randint(0,1) # 1 и 0 это True = 1 и False = 0
    print(name)
    if name: # означает истинно, а значит True = 1
        print(f"Первый ходит {player1}")
    else: # это лож, а False = 0
        print(f"Второй ходит {player2}")
    count = 0
    konfet = 100
    counter1 = 0
    counter2 = 0
    while konfet > 0 and konfet > 28: 
            if name: # и здесь так же пользуемся, потому что не за что привязать больше count
                count = 1
                counter1 = random.randint(1,28) 
                print(f'Ваш ход {player1}, вы забирали {counter1} конфет') 
                konfet -= counter1 
                name = False # дает возможность переключать игроков в подобных условиях
            else:      
                counter2 = random.randint(1,28)
                count = 0
                print(f'Ваш ход {player2}, вы забирали {counter2} конфет') 
                konfet -= counter2
                name = True # дает возможность переключать игроков в подобных условиях
                print(f'Осталось конфет', konfet)
    if konfet <= 28: 
        if count == 0: print(f'Остается всего {konfet} , Ход переходит к вам {player1},\n{player1} забирает все остальные конфеты, вы победиль') # делаем наоборот, кто из рандомов брал последний и оставил конфеты тот и проиграл
        if count == 1: print(f'Остается всего {konfet} , Ход переходит к вам {player2},\n{player2} забирает все остальные конфеты, вы победиль')
    return konfet

reshenie2()