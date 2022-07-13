# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

def lengt(Ax1, Ay1, Bx2, By2):
    return round(math.sqrt((Bx2-Ax1)**2+(By2-Ay1)**2), 2)

Ax1 = float(input('Введите координаты Aх1 \n'))
Ay1 = float(input('Введите координаты Ay1 \n'))
Bx2 = float(input('Введите координаты Bx2 \n'))
By2 = float(input('Введите координаты By2 \n'))

print(lengt(Ax1, Ay1, Bx2, By2))
# print('{:.2f}'.format(result), sep='')



# 2 варинат
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# def length(x1, y1, x2, y2):
#     ab = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     print(ab)
# length(x1, y1, x2, y2)
