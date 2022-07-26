# 32. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10, 7] => [2, 10]

def spisk():
    my = [1, 2, 3, 5, 1, 5, 3, 10, 7]
    my2 = []
    gif = {}
    print (my)
    for i in my:
        gif = {i: my.count(i)}
        for key, value in gif.items():
          if value == 1: my2.append(key)
    print(my2)
    return gif
spisk()


def spisok():
    my = [1, 2, 3, 5, 1, 5, 3, 10, 7]
    frg = []
    print (my)
    for i in my:
        if  my.count(i) == 1:
            frg.append(i)
    print(frg)
    return frg
spisok()
  


# Mylist = [1, 2, 3, 5, 1, 5, 3, 10, 7]
# def unik(Mylist):
#     result = []
#     for i in Mylist:
#         if Mylist.count(i) == 1:
#             result.append(i)
#     return result
# print(unik(Mylist))


# numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
# def UniqueNumbers(numbers):
#     result=[i for i in numbers if numbers.count(i)==1]
#     return result
# print(UniqueNumbers(numbers))



# # сделать словарями

# def uniks(Mylist):
#     result = []
#     count = 0
#     for i in Mylist:
#         count = 1
#         for x in i:
#             if x == i:
#                 count += 1
#     if count == 2:
#                 result.append(i)
#     return result
# print(uniks(Mylist))
