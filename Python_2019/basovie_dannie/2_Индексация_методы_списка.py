# 2_Индексация_списка

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list([1,2,3,4])) # [1, 2, 3, 4]
print(list(range(5, 10 ,2))) # [5, 7, 9]

# 2_методы списка 
# count
my_list = [1,2,3,4,5, 'WERF', 6,7,8,9,5]
print(my_list.count(5)) # 2 две пятерки у нас
my_list.extend([4,5,6,7])
print(my_list) # [1, 2, 3, 4, 5, 'WERF', 6, 7, 8, 9, 5, 4, 5, 6, 7] добавил элементы
print(my_list.count(5)) # 3

# min max 
del my_list[5] # для подсчета максимального и минимального надо удалить текст из списка
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 5, 6, 7]
print(min(my_list)) # 1
print(max(my_list)) # 9

# сортировка списка sort
my_list.insert(1, 144)
print(my_list) # [1, 144, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 5, 6, 7] поставили после 1 элемента 144
my_list.sort()
print(my_list) # [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 9, 144] отсортировался 
my_list.pop() 