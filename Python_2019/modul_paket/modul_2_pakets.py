# 5.5 Пакеты и способы создания. Часть 1
"----------------------------------------"

# К модулям мы можем обращаться через точку
from pprint import pprint
from moduli.modul_1 import function1

function1() # из папки  modul_paket взяли модуль modul_1 через точку и из этого модуля взяли функцию function1

# можно напрямую сделать 
import moduli.modul_1 # но тогда точно такой же путь придется использовать в вызове
moduli.modul_1.function1()

import moduli.modul_1 as p1m1 # можно создать синонемы
p1m1.function1() # так вот с папкамии подпапками можно работать

import moduli
moduli.modul_1.function1() # вот так можно еще сделать


from moduli.sub import modul_2
modul_2.function1() # HEY!!!

from moduli.sub.modul_2 import function1
function1()

import moduli.sub as ms
ms.modul_2.function1() 

import moduli.sub.modul_2 as msm 
msm.function1() 
pprint([])

# from .modul_1 import function1 #. значит обратиться к нашей дирректории. а .. к родительской
# function1()
# # если нужно обратить на уровень выше то пишем

# from ..modul_1 import function1


