# re.split 
# re.split (pattern, string, maxsplit=0, flags=0)
# Разделяет строку на части опираясь на символ разделитель и возвращается список подстрок
# разобьем строку на части, а в качестве разделителя выберем запятую
import re

test_string4 = 'Django, Flack, FastAPI, Tornado, Aiohttp, Sanic'
print(test_string4 )
splited_sstring_list = re.split(r',', test_string4)

print('Список фруймворков: ', splited_sstring_list)
print('Первый фруймворков: ', splited_sstring_list[0] + splited_sstring_list[1])