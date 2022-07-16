# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. сохраните список в формате JSON.


import random
import json

# n = int(input('введите n'))
n = random.randint(3,10)
def spisok(n):
    return [i for i in range(-n, n+1)]
    return list(range(-n, n+1))
print(spisok(n))
spisk = spisok(n)


with open('data.json', 'w', encoding='utf-8') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write(json.dumps(spisk))
print('БД успещно загружена')

# with open('data.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
#     data.write(spisk)

# with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD = json.load(fh)  # загружаем из файла данные в словарь data
# print('БД успещно загружена')
# print(type(BD))



# import json
# from os import lstat 
# n = random.randint(3,10)
# # n = int(input( ' введите число n -> '))
# spisok = list(range(-n, n+1))

# print(spisok)

# with open('list.json', 'a', encoding='utf-8') as sh:  # открываем файл на чтение
#       sh.write(json.dumps(spisok, ensure_ascii=False))
#   # загружаем из файла данные в словарь data
# print('список успешно загружен')
# # print(type(sh))


    

