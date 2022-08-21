# Метод считывает и возвращает считанные данные с файла file_name
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# Метод позволяет записать текст в файл
def write_file(text):
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.txt', 'a+', encoding='utf-8') as file:
        file.write(text + '\n')


# def log_data(s):
#     dt = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
#     s = 'Дата и время:' + ' ' + dt + '; ' + s + '\n'
#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar7\log_file.txt', 'a', encoding='utf-8') as l:
#         l.write(s)




def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# file1 = 'polynomial.txt'
# file2 = 'polynomial2.txt'

# print(sborka(newlist))
# temp = sborka(newlist) 

# file_end = temp # создаем файл и передаем значения нашего полинома
# with open('polynomial_end.txt', 'w') as data:
#     data.write(file_end)