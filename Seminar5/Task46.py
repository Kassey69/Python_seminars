# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".



text = 'амбуцмен, ишакабв, катрина, геркуабвлес'
text = text.split()

text2 = 'амбуцмен, ишакабв, катрина, геркуабвлес'.replace('абв','')
print(text2)

def del_stroka(text):
    result = ''
    x = 'абв'
    for i in text:
        if x not in i: result += str(i) + ' '
    print(result)
    return result
del_stroka(text)



# text = 'арбуз друг абв лежал на столеабв'
# text = text.split() # разбить на элементам, не забываем скобки
# print(text)
# def delet(text):
#     x = "абв"
#     res = ''
#     for i in text:
#         if x not in i:
#             res += str(i) + ' '       
#     return res
# print(delet(text))


# прежде чем циклировать слова нужно их разбить text.split()  = ' амбуцмен, ишакабв, катрина, геркуабвлес'

# text = 'арбуз друг абв лежал на столеабв'.replace('абв','') # так удаляется любой фрагмент из любых слов
# print(text)



