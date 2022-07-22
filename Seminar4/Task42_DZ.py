# 3 (необязательное). Напишите программу, которая принимает на стандартный вход список игр 
# футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6



from audioop import reverse


def tablis(myl):
    n = 1
    slovar = {}
    for i in range(n): 
        d = {myl[0]:myl[1], myl[2]:myl[3]}
        win = ''
        if myl[1] > myl[3]: win = myl[0]
        elif myl[1] < myl[3]: win = myl[2]

        for key in d.keys(): # тоже самое что и d только работает намного быстрее, не занимая много памяти
            if key not in slovar.keys():
                slovar.update({key:[0, 0, 0, 0, 0]})
            slovar.get(key)[0] +=1
            if key == win: slovar.get(key)[1] +=1 
            elif win == '': 
                
                slovar.get(key)[2] += 1
            else: slovar.get(key)[3] += 1  

    for key in slovar.keys():
        slovar.get(key)[4] = slovar.get(key)[1]*3 + slovar.get(key)[2]
        print(key, end=':')
        for i in range(5):
            print(slovar.get(key)[i], end=' ')
        print()    
    return slovar  

def crez1(myl):
    slov1 = {}
    a = slov1.fromkeys([myl[0]],  [2, 0, 0, 2, 0])
    slov1.update(a)
    for key in slov1.keys():
            print(key, end=':')
            for i in range(5):   
                print(slov1.get(key)[i], end=' ') 
    print()           
    return myl

def crez2(myl):
    slov2 = {}
    a = slov2.fromkeys([myl[0]],  [2, 1, 0, 1, 3])
    slov2.update(a)
    for key in slov2.keys():
            print(key, end=':')
            for i in range(5):
                print(slov2.get(key)[i], end=' ')       
    print()
    return myl

def crez3(myl):
    slov3 = {}
    a = slov3.fromkeys([myl[0]],  [2, 2, 0, 0, 6])
    slov3.update(a)
    for key in slov3.keys():
            print(key, end=':')
            for i in range(5):
                print(slov3.get(key)[i], end=' ') 
    print()
    return myl

    # Вводим значения
tablis(myl = ['Спартак  ',9,'Зенит    ',10])
print("-------------------")
tablis(myl = ['Локомотив',12,'Зенит    ',3])
print("-------------------")
tablis(myl = ['Спартак  ',8,'Локомотив',15])
print("------------------------------")
print("  Общяя статистика ")
crez1(myl = ['Спартак  '])
crez2(myl = ['Зенит    '])
crez3(myl = ['Локомотив'])















# col = int(input())
# spi = []
# slov = {}

# def newUpdate(oldValue, newValue):
#     s = oldValue.copy()
#     for i in range(5):
#         s[i] += newValue[i]
#     return s

# for i in range(col):
#     # team = input().split(';')
#     team = [1, 10, 2, 3]
#     team[1], team[3] = int(team[1]), int(team[3])
#     spi.append(team)
#     a = slov.fromkeys([team[0], team[2]], [0, 0, 0, 0, 0])
#     slov.update(a)

# for i in range(len(spi)):
#     if spi[i][1] > spi[i][3]:
#         tmp = newUpdate(slov[spi[i][0]], [1, 1, 0, 0, 3])
#         slov.update({spi[i][0]: tmp})

#         tmp = newUpdate(slov[spi[i][2]], [1, 0, 0, 1, 0])
#         slov.update({spi[i][2]: tmp})
#     elif spi[i][1] == spi[i][3]:
#         tmp = newUpdate(slov[spi[i][0]], [1, 0, 1, 0, 1])
#         slov.update({spi[i][0]: tmp})

#         tmp = newUpdate(slov[spi[i][2]], [1, 0, 1, 0, 1])
#         slov.update({spi[i][2]: tmp})
#     else:
#         tmp = newUpdate(slov[spi[i][2]], [1, 1, 0, 0, 3])
#         slov.update({spi[i][2]: tmp})

#         tmp = newUpdate(slov[spi[i][0]], [1, 0, 0, 1, 0])
#         slov.update({spi[i][0]: tmp})

# print(slov)









# # put your python code here
# # games = int(input())
# games = 1
# results = {}
# for n in range(games):
#     # line = input()
#     line = "1;1;2;2"
#     line = line.split(";") 
#     print(line)
#     for i in range(0,3,2): 
#         if line[i] not in results: 
#             results[line[i]] = [1, 0, 0, 0, 0] 
#         else: 
#             results[line[i]][0] += 1 
#         if line[1] > line[3]: 
#             results[line[0]][1] += 1 
#             results[line[2]][3] += 1 
#         elif line[1] == line[3]: 
#             results[line[0]][2] += 1 
#             results[line[2]][2] += 1 
#     else: 
#             results[line[0]][3] += 1 
#             results[line[2]][1] += 1 
 
# for team, res in results.items(): 
#         res[4] = res[1]*3 + res[2] 
#         print(team+":", res[0], res[1], res[2], res[3], res[4]) 





