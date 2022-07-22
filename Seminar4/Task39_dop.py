# sp = [1, 6.8, 11, 'dsafsd', True]

# for i in sp:
#     print(i, end = ' ')

# for i in range(len(sp)):
#     print(i, sp[i])






# Задаем ввод только числа

# def vvod():
#     while True:
#         try: # если условие что ниже не сработает то перейдем в исключения except:
#                 x = input('Введите число\n')
#                 x = float(x)
#                 return x
#         except: # исключения
#             print('Сказали же число')  
# ret =  vvod() 
# print(ret) # 4.0

# ret = (int(str(ret).replace('.','')))//10    # убрали запятую и лишний нолик дщелением нацело

# print(f'ура', ret) # ура 4


# Перемешаем значения
from random import *
spp = [1, 6.8, 11, 'dsafsd', True]

def shuffle(sp):
    for i in range(25):
        buf = 0
        x = randint(0,len(sp)-1)
        y = randint(0,len(sp)-1)
        buf = sp[x]
        sp[x]=sp[y]
        sp[y]=buf
    return sp

shuffle(spp)
print(spp)


# Введите числа через пробел c помощью фикла for

a = input('Введите числа через пробел\n')
а = [int(i) for i in a.split()]
a = list(str(a)) # ['3', ' ', '2', '3', ' ', '2']
a = ''.join(a).replace(' ', '') # 3232 сократили между ними пробелы
# a = list(map(int, input('Введите числа через пробел\n').split()))
print(a)








