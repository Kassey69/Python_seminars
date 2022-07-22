# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 
# Привер 30 = 3 * 2 * 5

from random import randint

n = randint(2,1000)
def znach(n): 
    l = []
    d = []
    znachenie = [1] # добавляем 1 как множитель для чисел где n % i != 0
    count = 0 
    for i in range(2,n):
        for x in range(i):       # делаем дополнительные проходы для поиска одинаковых численных множителей
                if n % i == 0:
                    count = 1    # создаем один из варинатов чтоб потом вызвать и присвоить значение переменных
                    l.append(i) 
                    n = n // i  

                elif n % i != 0:                 
                    d.append(i)  

    if count == 1: znachenie = l
    else: znachenie.append(n)                                                                             
    return znachenie

temp = znach(n)  
res = ' '.join(map(str,temp)) # убираем скобки
result =f"Cписок простых множителей числа: {n} = {res.replace(' ', ' * ') }" # заменяем пустые пробелы на умножение
print(result)

  











# n = 20
# def znach(n):
#     l = []
#     i = 1
#     while True:
#         if n > 0:
        
#             if n % i == 0: 
#                l.append(i) 
#                n = n // i                    
#             i += 1 
#         else:
#             print(l) 
#     return l       
  

znach(n)


# import math

# def is_prime(n):
#     primes = [2]
#     for num in range(3, n + 1, 2):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
#             primes.append(num)
#     return primes

# def get_prime_factors(n, primes):
#     fact = []
#     for i in primes:
#         while n % i == 0:
#             n = n / i
#             fact.append(i)
#     return fact

# n = int(input('Введите число: '))

# primes = is_prime(n)
# factors = get_prime_factors(n, primes)
# print(factors)

# def testing(n, factors):
#     return math.prod(factors) == n       

# print(testing(n, factors))

# def task31 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)

# print (task31 (5))