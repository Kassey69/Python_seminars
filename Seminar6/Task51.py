# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# aaaaddbbb  - 4a2d3b


text = 'ssssssssssssssssskkkkkfryyyyyttt'   

def sets(text):
    lists = [text[i] for i in range(len(text))] # ['a', 'a', 'a', 'a', 'd', 'd', 'b', 'b', 'b']
    # print(lists)
    # r = (max(set(lists[x]), key = lambda x: lists.count(x)))
    # return r
    analize = ''
    counts = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            counts += 1
        else:
            analize += str(counts) + lists[i]
            counts = 1 # обнуляем counts
    # print(analize) # 5s5k1f1r5y
    if counts > 1 or (lists[len(lists)-2] != lists[-1]):
        analize +=  str(counts) + lists[-1]         # добавляет последний элемент
    # print (analize) # 5s5k1f1r5y3t
    return analize

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha(): # Метод str.isalpha()проверяет, что строка состоит только из буквенных символов.
            number += txt[i]
            # print(number)
        else:
            res += txt[i] * int(number) # сначала все aaaa потом aaaadddddd и так далее
            # print(res)
            number = '' # чтоб не зависло все. очень много символов полетит
    return res

print(f'Сжатый модуль {sets(text)}')
print(f'Восстановление данных {decoding(sets(text))}')