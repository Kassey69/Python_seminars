# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python

# Дискриминант квадратного уравнения — это выражение, равное b2 − 4ac

import math
import random
def rand(znach):
        znach = round(random.uniform(-10, 10),1) # вариант с вещественными числами
        if znach == 0: # вдруг попадается ноль мы крутим рандом по новой
            znach = round(random.uniform(1, 10),1)
        return znach 

# формула дискриминанта = D = b^2 - 4ac

def sqrt_dis(a,b,c):
    print(f'Находим корни квардратного уравнения: {a}x^2 + {b}x + {c} = 0')
    dis = b ** 2 - 4 * a * c
    print(f'Дискриминант: {round(dis,2)}')
    sqrt_val = math.sqrt(abs(dis)) # получаем корень и подставляем при желании его везде
    print(f'Корень от дискриминанта', round(sqrt_val,4)) # корень от дискриминанта
    if dis < 0:
        print(f'Корней нет') 
    elif dis == 0:
        kor = round((- b / 2 * a),4)
        print(f'Один корень: {kor}')
    elif dis > 0 :
        kor1 = round(((-b + sqrt_val) / (2 * a )),4)
        kor2 = round(((-b - sqrt_val) / (2 * a )),4)
        print(f'1 корень X1: {kor1} \n2 корень X2: {kor2}')
    return a,b,c

znachie = [] 
a, b, c = [rand(znachie) for i in range(3)]
sqrt_dis(a, b, c) 


# a1 = rand(znachie)
# b1 = rand(znachie) 
# c1 = rand(znachie)
# sqrt_dis(a, b, c) 
# sqrt_dis(a1,b1,c1)       

# znachie = []  #создаем список, в него будут переходить значения с функции rand рандома
# a1 = rand(znachie) # нагружаем список рандомным значением от функции rand и передаем аргументам
# b1 = rand(znachie) 
# c1 = rand(znachie)
# sqrt_dis(a1,b1,c1) # если работать без return то получается как в си шарпе void, мы подключаем все вычисления
# производимые в функции sqrt_dis к 3 значениям, функция получает значения рандомные и вычисляет изнутри себя
# выдает внутренние print


