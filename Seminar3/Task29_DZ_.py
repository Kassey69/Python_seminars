# (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом 
# и вывести получившуюся статистику.

# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова 
# в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

# text = 'a aa abC aa ac abc bcd a'.lower().split()
# text = [i.lower() for i in input().split()]


text = list(map(str, input(f'Введите строчку\n').lower().split()))

print(text) # ['a', 'aa', 'abc', 'aa', 'ac', 'abc', 'bcd', 'a']
def texts(text):
    string = {}
    for i in set(text): # set убирает всех двойников
        string = {i:text.count(i)} # i это ключ,а text.count(i) подсчет количества (count) значений в каждом ключе строки
        for key, value in string.items(): # цикле for использует метод items() для получения пары «ключ — значение» на каждую итерацию.
            print(f'({key}:{value})', end=' ') # keys() — возвращает ключи, values() — возвращает список значений словаря
    return string 
texts(text)

'''ВСЕ О СЛОВАРЯХ  САЙТ - https://webdevblog.ru/kak-perebrat-slovar-v-python/'''

# Изменение регистра символов в строках Python
# Одна из простейших операций при работе со строками это — изменение регистра. 
# Сейчас мы рассмотрим три метода, которые позволяют изменять регистр строк:

# title() — каждое слово в строке начинается с заглавной буквы;
# lower() — текст переводится в нижний регистр;
# upper() — текст переводится в верхний регистр;
# swapcase() – переводит символы верхнего регистра в нижний, а нижний в верхний;
# capitalize() – переводит первый символ строки в верхний регистр, а остальные символы в нижний;

# Методы словарей в Python
# Перечислим основные словарные методы, которые помогут вам при работе с этим типом данных.

# clear() — очищает заданный словарь, приводя его к пустому.
# get() — отдаёт значение словаря по указанному ключу. Если ключ не существует, а в качестве дополнительного аргумента передано значение по умолчанию, то метод вернет его. Если же значение по умолчанию опущено, метод вернет None.
# items() — возвращает словарные пары ключ:значение, как соответствующие им кортежи.
# keys() — возвращает ключи словаря, организованные в виде списка.
# values() — подобным образом, возвращает список значений словаря.
# pop() — удалит запись словаря по ключу и вернет её значение.
# popitem() — выбрасывает пару ключ:значение из словаря и возвращает её в качестве кортежа. Такие пары возвращаются в порядке LIFO.
# update() — реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения одного словаря с ключами и значениями другого. При этом если какие-то ключи совпадут, то результирующим значением станет значение словаря, указанного в качестве аргумента метода update.
# copy() — создает полную копию исходного словаря.


# Словари сопоставляют ключи со значениями и сохраняют их в массиве или коллекции.
# Ключи должны быть хэшируемого типа (hashable), что означает, что в качестве ключа используют хэш 
# значения ключа, который никогда не меняется в течение срока жизни ключа.



# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key in a_dict:
#     print(key)

# Объект представления, возвращаемый функцией .items(), выдает пары ключ-значение по одной и позволяет перебирать словарь, 
# и таким образом, вы получаете доступ к ключам и значениям одновременно.

# Если вы присмотритесь к отдельным элементам, полученным с помощью .items(), 
# вы заметите, что они действительно являются кортежами объектов.


# Если вам просто нужно работать с ключами словаря, то вы можете использовать метод .keys(), 
# который возвращает новый объект представления, содержащий ключи словаря:

# >>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# >>> keys = a_dict.keys()
# >>> keys
# dict_keys(['color', 'fruit', 'pet'])

# Чтобы перебрать словарь в Python с помощью .keys(), вам просто нужно вызвать .keys() в заголовке цикла for:

# >>> for key in a_dict.keys():
# ...     print(key)
# ...
# color
# fruit
# pet


# Итерация по .values() такая же как и с key!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# ключи могут быть добавлены или удалены из словаря путем преобразования представления, 
# возвращаемого функцией .keys(), в объект list:

# >>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# >>> for key in list(prices.keys()):  # Use a list instead of a view
# ...     if key == 'orange':
# ...         del prices[key]  # Delete a key from prices
# ...
# >>> prices
# {'apple': 0.4, 'banana': 0.25}


# Превращение ключей в значение и наоборот
# Предположим, у вас есть словарь и по какой-то причине необходимо превратить ключи в значения и наоборот.
#  В этой ситуации вы можете использовать цикл for для перебора словаря и создания нового словаря, 
#  используя ключи в качестве значений и наоборот:

# >>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# >>> new_dict = {}
# >>> for key, value in a_dict.items():
# ...     new_dict[value] = key
# ...
# >>> new_dict
# {1: 'one', 2: 'two', 3: 'thee', 4: 'four'}



# Фильтрация
# Иногда вы будете в ситуациях, когда у вас есть словарь, и вы захотите создать новый, 
# чтобы хранить только данные, которые удовлетворяют заданному условию. 
# Вы можете сделать это с помощью if внутри цикла for следующим образом:

# >>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# >>> new_dict = {}  # Create a new empty dictionary
# >>> for key, value in a_dict.items():
# ...     # If value satisfies the condition, then store it in new_dict
# ...     if value <= 2:
# ...         new_dict[key] = value
# ...
# >>> new_dict
# {'one': 1, 'two': 2}