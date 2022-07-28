# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# aaaaddbbb  - 4a2d3b
from collections import Counter
import re
from itertools import groupby


def modul_sjatia():
    text = 'ssssssssssssssssskkkkkfryyyyyttttsreeee' 
    text = text.replace('',' ').split() 
    print(text) # ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'k', 'k', 'k', 'k', 'k', 'f', 'r', 'y', 'y', 'y', 'y', 'y', 't', 't', 't']
    count = 1
    l = ''
    for i in range(len(text)-1): 
        if text[i] == text[i+1]:
            count +=1
        else: 
            l += str(count) + str(text[i])
            count = 1
    l = str(l) + str(count) + str(text[-1]) # нужно добавить не (text[i-1]) это ошибка!!! это не последний элемент, 
                                                            # а именно последний эдлемент text[-1]
    print(f'Модуль сжатия', l) #  Модуль сжатия 17s5k1f1r5y3t
    return l


def modul_vostanovlenia(l):
    a = re.findall(r'\d+', l) # отделяем цифры от букв
    b = re.findall(r'[A-Za-z]+', l) #  отделяем буквы от цифр
    # print(a) # '17', '5', '1', '1', '5', '3']
    # print(b) # ['s', 'k', 'f', 'r', 'y', 't']
    f = []
    for i, j in zip(a, b):
        f += [i, j] # сливаем и переводим в список
    # print(f) # ['17', 's', '5', 'k', '1', 'f', '1', 'r', '5', 'y', '3', 't']
    g = ''
    for i in range(len(f)):
        i = int(i)
        if i %2!=0:
            g += str(f[i] * int(f[i-1] ))
    print(f'Восстановление данных', g) # Восстановление данных ssssssssssssssssskkkkkfryyyyyttt
    return g

l = modul_sjatia()    
temp = modul_vostanovlenia(l)


file_mod1 = l # создаем файл и передаем значения нашего полинома
with open('modul_sjatia.txt', 'w') as data:
    data.write(file_mod1)

file_mod2 = temp # создаем файл и передаем значения нашего полинома
with open('modul_vostanovlenia', 'w') as data:
    data.write(file_mod2)










# def sets(text):
#     lists = [text[i] for i in range(len(text))] # ['a', 'a', 'a', 'a', 'd', 'd', 'b', 'b', 'b']
#     # print(lists)
#     # r = (max(set(lists[x]), key = lambda x: lists.count(x)))
#     # return r
#     analize = ''
#     counts = 1
#     for i in range(len(lists)-1):
#         if lists[i] == lists[i+1]:
#             counts += 1
#         else:
#             analize += str(counts) + lists[i]
#             counts = 1 # обнуляем counts
#     # print(analize) # 5s5k1f1r5y
#     if counts > 1 or (lists[len(lists)-2] != lists[-1]):
#         analize +=  str(counts) + lists[-1]         # добавляет последний элемент
#     # print (analize) # 5s5k1f1r5y3t
#     return analize

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha(): # Метод str.isalpha()проверяет, что строка состоит только из буквенных символов.
#             number += txt[i]
#             # print(number)
#         else:
#             res += txt[i] * int(number) # сначала все aaaa потом aaaadddddd и так далее
#             # print(res)
#             number = '' # чтоб не зависло все. очень много символов полетит
#     return res

# print(f'Сжатый модуль {sets(text)}')
# print(f'Восстановление данных {decoding(sets(text))}')