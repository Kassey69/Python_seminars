# Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

from random import randint

# trext = [1, 5, 2, 3, 4, 6, 1, 7]

def spisok():
    n = randint(5,10)
    trext = []
    for i in range(n):
       trext.append(randint(1,9))
    print(trext) # получили рандомный список
    my = []
    for i in range(len(trext)-1):
        if trext[i] < trext[i+1] and trext[i] not in my and trext[i+1] not in my:
            d = {trext[i]: trext[i+1]} # создали словарь из 2 нужных элементов списка
            my.append(d)
    return my[:1:] # значит 1 элемент и стоп - slice(start, stop, step).
print(spisok())

    




















# def posled(trext):
#     dert = []
#     for i in range(len(trext)):
#         if trext[i] == max(trext[:i+1:]) and trext[i] not in dert:
#             dert.append(trext[i])     
#     # dert = [trext[i] for i in range(len(trext)) if trext[i] == max(trext[:i+1:]) and trext[i] not in dert]
#     return dert
# print(posled(trext))


# def posled(data):
#     dot = []
#     maxs = data[0]
#     for i in data:
#         if i >= maxs: 
#             maxs = i
#             dot.append(maxs)
#     return dot
# print(posled(trext))





# print(get_up(nums))

# nums = [1, 5, 2, 3, 4, 6, 1, 7]
# def get_up2(nums):
#     ups = [nums[0]]
#     for i in nums:
#         if i > max(ups):
#             ups.append(i)
#     return ups
    
# print(get_up2(nums))

