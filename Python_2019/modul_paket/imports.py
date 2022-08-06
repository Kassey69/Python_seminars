import modul_1 # перенесли модуль
import modul_1 as m # устанавливаем синоним, меняем название модуля и через точку мы можем использовать атрибут

# можно импортировать конкретные элементы
from modul_1 import function1, variable_1 # из этого модуля импортируй эти жлементы функций и размести их в текущем пространстве имен
function1()
print(variable_1)

# вариант с элементами функций
from modul_1 import function1 as f1, variable_1 as v1 # импортируем функции и имзменяем функциям имена
f1()
print(v1)

# импорт звездочка * это плохой стиль
from modul_1 import * # импортировать все имена из модуля с помощью звездоски 
function1()
print(variable_1)

# срабатывает всегда последнее определение функции которая стоит ниже

def function1():
    print('HEY')
    # если будет так 
from modul_1 import * # - то она перекроет верхнюю


# библиотеки пайтон https://docs.python.org/3/library/index.html

import math
import sys
from pprint import pprint

pprint(sys.path)
print(math.sin(90))

def some_funk():
    from math import sin
    return sin(0)

print(some_funk()) # вызвали сразу синус импортом