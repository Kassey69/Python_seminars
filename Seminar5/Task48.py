# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


text = 'арбуз друг абв лежал на столеабв'
text = text.split() # разбить на элементам, не забываем скобки
print(text)
def delet(text):
    x = "абв"
    res = ''
    for i in text:
        if x not in i:
            res += str(i) + ' '       
    return res
print(delet(text))


text = 'арбуз друг абв лежал на столеабв'.replace('абв','') # так удаляется любой фрагмент из любых слов
print(text)