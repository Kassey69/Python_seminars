# Создать программу игры в крестики нолики

import numpy as p
import random

def prover():
    x = input('Введите цифру от 1 до 9\nВвод: ')
    while True:
        try:
            x = int(x)
            if x < 1 or x > 9: # тут можно ввести три числа 2 3 и 4 которое понадобится для цикла while и выхода
                x = input('Введите корректное число\n')   
            else:
                break
        except ValueError: 
            x = input("Вы ввели не число. Повторите ввод\n")
    return x

def bul():
    from itertools import count as count_from
    count = count_from(1)
    a = [[next(count) for i in range(3)] for j in range(3)]
    # a = []
    # for i in range(0,3):
    #     temp = []
    #     for j in range(0,3):
    #         temp.append(next(count))
    #     a.append(temp)
    print((p.array(a)))

         

    player1 = 'Дмитрий'
    player2 = 'Борис' 
    name = random.choice([0, 1])
        # print( count)
    if name:
        print(f"Первый ходит {player1}") 
    if not name: 
        print(f"Первый ходит {player2}")
    count = 0
    while count != 3:   
        if name:
            print(f'Ваш ход Дмитрий')
            operas = prover() # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print(operas)
            if operas == 1 and a[0][0] != 'X' and a[0][0] != 'O': 
                a[0][0] = 'X' 
                name = False
            elif operas == 2 and a[0][1] != 'X' and a[0][1] != 'O': 
                a[0][1] = 'X'
                name = False
            elif operas == 3 and a[0][2] != 'X' and a[0][2] != 'O': 
                a[0][2] = 'X'
                name = False
            elif operas == 4 and a[1][0] != 'X' and a[1][0] != 'O': 
                a[1][0] = 'X'
                name = False
            elif operas == 5 and a[1][1] != 'X' and a[1][1] != 'O': 
                a[1][1] = 'X'
                name = False
            elif operas == 6 and a[1][2] != 'X' and a[1][2] != 'O': 
                a[1][2] = 'X'
                name = False
            elif operas == 7 and a[2][0] != 'X' and a[2][0] != 'O': 
                a[2][0] = 'X'
                name = False
            elif operas == 8 and a[2][1] != 'X' and a[2][1] != 'O': 
                a[2][1] = 'X'
                name = False
            elif operas == 9 and a[2][2] != 'X' and a[2][2] != 'O': 
                a[2][2] = 'X'
                name = False
            else: 
                name = True    
            b = p.transpose(a)
            print(p.array(b))            
        else: 
            print(f'Ваш ход Борис')    
            operas = prover()
            print(operas)
            if operas == 1 and a[0][0] != 'X' and a[0][0] != 'O': 
                        a[0][0] = 'O'
                        name = True
            elif operas == 2 and a[0][1] != 'X' and a[0][1] != 'O': 
                    a[0][1] = 'O'   
                    name = True                    
            elif operas == 3 and a[0][2] != 'X' and a[0][2] != 'O': 
                    a[0][2] = 'O'
                    name = True                  
            elif operas == 4 and a[1][0] != 'X' and a[1][0] != 'O': 
                    a[1][0] = 'O'
                    name = True                
            elif operas == 5 and a[1][1] != 'X' and a[1][1] != 'O': 
                a[1][1] = 'O'
                name = True           
            elif operas == 6 and a[1][2] != 'X' and a[1][2] != 'O': 
                a[1][2] = 'O'
                name = True
            elif operas == 7 and a[2][0] != 'X' and a[2][0] != 'O': 
                a[2][0] = 'O'
                name = True
            elif operas == 8 and a[2][1] != 'X' and a[2][1] != 'O': 
                a[2][1] = 'O'
                name = True
            elif operas == 9 and a[2][2] != 'X' and a[2][2] != 'O': 
                a[2][2] = 'O'
                name = True    
            else: 
                name = False
            b = p.transpose(a)
            print(p.array(b))    
            
        if a[0][0] == 'X' and a[0][1] == 'X'and a[0][2] == 'X':
            count == 3
            print(f'выиграл {player1}') 
            break
        elif a[1][0] == 'X' and a[1][1] == 'X'and a[1][2] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[2][0] == 'X' and a[2][1] == 'X'and a[2][2] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[0][0] == 'X' and a[1][0] == 'X'and a[2][0] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[0][1] == 'X' and a[1][1] == 'X'and a[2][1] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[0][2] == 'X' and a[1][2] == 'X'and a[2][2] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[0][0] == 'X' and a[1][1] == 'X'and a[2][2] == 'X':
            print(f'выиграл {player1}')
            count == 3
            break
        elif a[2][0] == 'X' and a[1][1] == 'X'and a[0][2] == 'X':    
            print(f'выиграл {player1}')
            count == 3
            break     

        if a[0][0] == 'O' and a[0][1] == 'O'and a[0][2] == 'O':
            count == 3
            print(f'выиграл {player2}') 
            break
        elif a[1][0] == 'O' and a[1][1] == 'O'and a[1][2] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[2][0] == 'O' and a[2][1] == 'O'and a[2][2] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[0][0] == 'O' and a[1][0] == 'O'and a[2][0] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[0][1] == 'O' and a[1][1] == 'O'and a[2][1] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[0][2] == 'O' and a[1][2] == 'O'and a[2][2] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[0][0] == 'O' and a[1][1] == 'O'and a[2][2] == 'O':
            print(f'выиграл {player2}')
            count == 3
            break
        elif a[2][0] == 'O' and a[1][1] == 'O'and a[0][2] == 'O':    
            print(f'выиграл {player2}')
            count == 3
            break 

        else:
            if (a[0][0] =='X' or a[0][0] =='O') and (a[0][1] =='X' or a[0][1] =='O') and (a[0][2] =='X' or a[0][2] =='O')\
                and (a[1][0] =='X' or a[1][0] =='O') and (a[1][1] =='X' or a[1][1] =='O') and (a[1][2] =='X' or a[1][2] =='0')\
                and (a[2][0] =='X' or a[2][0] =='O') and (a[2][1] =='X' or a[2][1] =='O') and (a[2][2] =='X' or a[2][2] =='0'):
                print('Ни одна команда не смогла выиграть, ничья')
                count == 3
                break
    return player1, player2, operas

bul()        


# разоюбрать потом  вариант крестиков ноликов https://pythonpip.ru/examples/kak-sdelat-igru-krestiki-noliki-na-python-primer-ishodnogo-koda
# http://pythonicway.com/?catid=0&id=4
      




