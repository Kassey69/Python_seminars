# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
    
#     *Пример:*
    
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint


My_list = []

def rand_spisok(My_list):
    n = randint(5,10) # сколько ячеек
    My_list = [randint(1,10) for i in range(n)] #  заполнение ячеек
    print(My_list)
    return My_list

def numbers(number):    
    return [number[i] for i in range(len(number)) if i % 2 != 0]

rand_My_list = rand_spisok(My_list)

num = numbers(rand_My_list)
print(f'Элементы стоящие на нечётных позициях:', numbers(rand_My_list))
print(f'Cумма элементов списка =', sum(numbers(rand_My_list)))



# ls = [2, 3, 5, 9, 3]
# def ls_sum(a):
#     result = 0
#     for i in range(len(a)):
#         if i % 2 != 0:
#             result += int(a[i])
#     print(result)

# ls_sum(ls)
