# 1 воины 2  здоровье - 100 и атака - 20
# идет бой . и они сражаются. 
# удар 10 атаки

from random import randint
import random 

gandalf={}
balrog={}
gandalf['attack']=10
gandalf['hp']=50
balrog['attack']=7
balrog['hp']=70
count = 0
print('начало')

name = 1 # 1 и 0 это True = 1 и False = 0
if name: # означает истинно, а значит True = 1
    print('у гендальфа  ', gandalf['hp'],'здоровья')
    print('у балрога ', balrog['hp'],'здоровья')
else: # это лож, а False = 0
    print(f"Начинаем ")

while gandalf['hp'] > 0 and balrog['hp'] > 0:
        names = random.choice([0, 1])
        if names == 0:
            if name:
                if balrog['hp'] <= 0: break
                else:
                    count = 1
                    dop_udar_gandalf = randint(0, gandalf['attack'])
                    balrog['hp']-=gandalf['attack'] + dop_udar_gandalf
                    print(f'атака гендальфа', gandalf['attack'] + dop_udar_gandalf)
                    print('у балрога осталось ', balrog['hp'],'здоровья')
                    print('у гендальфа осталось ', gandalf['hp'],'здоровья')
                    name = False
            else:   
                if gandalf['hp'] <= 0: break
                else:
                    count = 0
                    dop_udar_balrog = randint(0, balrog['attack'] )
                    gandalf['hp']-=balrog['attack'] + dop_udar_balrog 
                    print(f'атака балрога', balrog['attack'] + dop_udar_balrog)
                    print('у гендальфа осталось ', gandalf['hp'],'здоровья')
                    print('у балрога осталось ', balrog['hp'],'здоровья')
                    name = False
        else:
            if name:
                if gandalf['hp'] <= 0: break
                else:
                    count = 0
                    dop_udar_balrog = randint(0, balrog['attack'] )
                    gandalf['hp']-=balrog['attack'] + dop_udar_balrog 
                    print(f'атака балрога', balrog['attack'] + dop_udar_balrog)
                    print('у гендальфа осталось ', gandalf['hp'],'здоровья')
                    print('у балрога осталось ', balrog['hp'],'здоровья')
                    name = False            
            else:
                if balrog['hp'] <= 0: break
                else:
                    count = 1
                    dop_udar_gandalf = randint(0, gandalf['attack'])
                    balrog['hp']-=gandalf['attack'] + dop_udar_gandalf
                    print(f'атака гендальфа', gandalf['attack'] + dop_udar_gandalf)
                    print('у балрога осталось ', balrog['hp'],'здоровья')
                    print('у гендальфа осталось ', gandalf['hp'],'здоровья')  
                    name = True               
if gandalf['hp'] <= 0 and balrog['hp'] <= 0:
    print(' оба трупы')
    
elif gandalf['hp'] <= 0 or balrog['hp'] <= 0:
    if count == 0: print(f' победил балрог')
    if count == 1: print(f'победил гендальф')

  