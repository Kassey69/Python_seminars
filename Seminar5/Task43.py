# 32. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10, 7] => [2, 10]

Mylist = [1, 2, 3, 5, 1, 5, 3, 10, 7]
def unik(Mylist):
    result = []
    for i in Mylist:
        if Mylist.count(i) == 1:
            result.append(i)
    return result
print(unik(Mylist))


numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
def UniqueNumbers(numbers):
    result=[i for i in numbers if numbers.count(i)==1]
    return result
print(UniqueNumbers(numbers))



# сделать словарями

def uniks(Mylist):
    result = []
    count = 0
    for i in Mylist:
        count = 1
        for x in i:
            if x == i:
                count += 1
    if count == 2:
                result.append(i)
    return result
print(uniks(Mylist))
