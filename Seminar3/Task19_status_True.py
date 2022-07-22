# Сделать функцию поторая на вход принимает список а возвращает словарь
# где 5 элементов
# мах
# мин
# индекс мах числа 
# индекс мин числа
# среднее арифметические'''

# sp = [5,4,33,2,18]

import json

status = True
while status != False:

    list_may = list(map(str, input(f'Введите набор чисел\n').split())) 

# def net_bykv(list_may):
    count = 0   
    for i in list_may:
        # if ( (c >= '0' and c <= '9') or (arg_one >= 'A' and arg_one <= 'Z') or (arg_one >= 'a' and arg_one <= 'z') or (arg_one >= 'A' and arg_one <= 'Я') or (arg_one >= 'а' and arg_one <= 'я'):
        if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Я') or (i >= 'а' and i <= 'я'):
                count = 1    
    if count == 1: 
            print(f'введите только числа, не должно быть букв')   
    else: status = False     
        # return list_may

def slovar(list_may):
    l = {}
    maxs = list_may[0]
    mins = list_may[0]
    index_maxs = 0
    index_mins = 0
    sums = 0
    for i in range(len(list_may)):
        if list_may[i] > maxs: 
            maxs = list_may[i]  # максимальный элемент
            index_maxs = i
        if list_may[i] < mins: 
            mins = list_may[i] # минимальный элемент
            index_mins = i
        sums += list_may[i] 
        sred_ar = round(sums/len(list_may),2)
    print(f'Вычисляем среднее арифметическое: (+ все значения): {sums} / {len(list_may)}(количество эдлементов) = {sred_ar}')
    # print(maxs, mins, index_maxs, index_mins, sred_ar)
    l ['макс. элемент '] = maxs
    l ['макс. индекс '] = index_maxs
    l ['мин. элемент '] = mins
    l ['мин. индекс '] = index_mins
    l ['сред. ариф. '] = sred_ar
    return l

def crezi(list_may): # пришлось все значения переводить в int потому что иначе не получалась проверка выше, тут деление+сложение
    number = [ int (i) for i in list_may]
    return number
    
print(crezi(list_may))
slovarik = (slovar(crezi(list_may)))
print(slovarik)


with open('data.json', 'w', encoding='utf-8') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write(json.dumps(slovarik))
print('БД успещно загружена')

# Метод split () возвращает список слов в строке, где разделителем по умолчанию является пробел. 
# Синтаксис. string.split (sep, maxsplit) sep: разделитель, используемый для разделения строки. 
# Если не указано иное, разделителем по умолчанию является пробел [на выбор] maxsplit: обозначает количество разделений.

'''# 2 рандомная начинка начала'''

# import random
# n = random.randint(3,10)
# list_may = []
# for i in range(n):
#     list_may.append(random.randint(1,10))
# list_may = [random.randint(1,10) for i in range(n)] # мы вводим наше значение в цикл, находясь внутри списка []

# list_may = [7, 5, 8, 4, 9]
# print(list_may)




# вариант 2 

N = 5

def inisp(N):
    sp = []
    for i in range(1,N+1):
        sp.append(round((1+1/i)**i,2))
    return sp

def inib(sp):
    bib = {}
    max = sp[0]
    idmax = 0
    min = sp[0]
    idmin = 0
    sum = 0
    for i in range(len(sp)):
        if(max<sp[i]):
            max = sp[i]
            idmax = i
        if(min>sp[i]):
            min = sp[i]
            idmin = i
        sum += sp[i]
    sred = sum/len(sp)
    bib['max'] = max
    bib['idmax'] = idmax
    bib['min'] = min
    bib['idmin'] = idmin
    bib['sred'] = sred
    return bib



spisok = inisp(N)
print(inib(spisok))  

spisok = inisp(N)
bibl = {}
print(spisok)
bibl = inib(spisok)
print(bibl)
# file = open('HW1.txt','a')
# for a,b in bibl.items():
#     file.write(f'{a} - {b} ')
# file.write('\n')
# # file.close()
