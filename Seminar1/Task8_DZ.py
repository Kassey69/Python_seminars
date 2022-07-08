# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# на платформу отправлять скрин выполнения кода первой и второй задачи + ссылку на репозиторий в гитхабе

import random

x = random.randint(-40,40)
y = random.randint(-40,40)
def coordinates_point(x, y):
    if x > 0 and y > 0: print(f'1 четверть x:{x} y:{y}')
    elif x < 0 and y > 0: print(f'2 четверть x:{x} y:{y}')
    elif x < 0 and y < 0: print(f'3 четверть x:{x} y:{y}')
    elif x > 0 and y < 0: print(f'4 четверть x:{x} y:{y}')
    elif (x > 0 or x < 0) and y == 0: print(f'ось x  x:{x} y:{y}')
    elif x == 0 and (y > 0 or y < 0): print(f'ось y  x:{x} y:{y}')
    else: print(f'значения введены некорректно x:{x} y:{y}')
    return x, y
coordinates_point(x, y)

