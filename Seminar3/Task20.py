# формат json
# все что мы загруждаем с джейсона либо словарь либо список

import json
sp=[5,11,2,3,4,8,157,555]

def max_average(sp):
    maxx=sp[0]
    sr=0
    for i in sp:
        if i > maxx:
            maxx=i
        sr+=i
    sr=sr/len(sp)
    rez={}
    rez['максимальный элемент']=maxx
    rez['среднее арифметическое']=sr
    k=(maxx,sr,rez)
    return k
print(max_average(sp))

with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD = json.load(fh)  # загружаем из файла данные в словарь data
print('БД успещно загружена')
print(type(BD))

