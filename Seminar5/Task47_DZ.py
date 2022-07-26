# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.

# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55

# то в итоге будет, 3*x^3 + 12*x^2+10*x+66


def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

file1 = 'polynomial.txt'
file2 = 'polynomial2.txt'

# 61x^3 + 43x^2 + 81x + 39 = 0
# 42x^4 + 81x^3 + 10x^2 + 10x + 41 = 0

print(read_pol(file1)) # показывают файл1, где находится запись многочлена
print(read_pol(file2)) # показывают файл2, где находится запись многочлена

def ondelenie_numbers(vvod):
    temp = vvod.replace(' + ', ' ').replace('= 0', '').split() # делаем для отдельного числа без x
    chislo_bez_x = []
    for i in temp:
        if 'x' not in i:
            chislo_bez_x.append(i) 
    # print(chislo_bez_x) # просчитали отдельное число без х   # ['39']

    pol = vvod.replace('= 0', '').replace('x^', ' ').replace('x', ' ').replace(' + ', ' ').split()
    # print(f'Убрали все знаки, оставили только числа',pol) # ['61', '3', '43', '2', '81', '39']
    string = {}
    st = []
    for i in range(len(pol)): 
        if i % 2 == 0: # за счет того что каждое значение парное, без последнего, состоящее из числа и степени за счет х, мы 
            string = {pol[i]: pol[i+1]} # создаем из них словарь, последнее 39 не учитывается, мы его отдельно посчитали
            # print(string) # {'61': '3'} {'43': '2'} {'81': '39'}
            for i, value in string.items(): # цикле for использует метод items() для получения пары «ключ — значение» на каждую итерацию.
                st.append(i) # ['61', '43', '81'], отставляем только ключи, созраняя их в списки
    # print(st) # ['61', '43', '81'] без последнего числа
    yravn = st + chislo_bez_x
    # print(yravn) # ['61', '43', '81', '39'] C ПАОСЛЕДНИМ ЧИСЛОМ
    return yravn

te1 = ondelenie_numbers(read_pol(file1)) # создаем файл отвечающий за отделение всего лишнего из выражения 1
te2 = ondelenie_numbers(read_pol(file2)) # создаем файл отвечающий за отделение всего лишнего из выражения 2
te1 = te1[::-1] # переворачиваем выражение 1 другой стороной, для подсчета индекса -> ['39', '81', '43', '61']
te2  = te2 [::-1] # переворачиваем выражение 2 другой стороной, для подсчета индекса -> ['41', '10', '10', '81', '42']

def slojenie(te1, te2):
    slovar3 = {}
    newslovar = {}
    newlist = []
    slovar1 = {i : te1[i] for i in range(len(te1))} # присвоили за счет словарей каддому числу индекс, его взяли как ключ
    slovar2 = {i : te2[i] for i in range(len(te2))}
    # for i in range(len(te1)):
    #     slovar1 = slovar1 + {i: te1[i]} 
    # print(slovar1) # {0: '39', 1: '81', 2: '43', 3: '61'}
    # print(slovar2) # {0: '41', 1: '10', 2: '10', 3: '81', 4: '42'}

    if len(slovar1.items()) > len(slovar2.items()): # опредлить длину словаря
        # print(f' кто длиннее 1строка',slovar1)  
        slovar3.update(slovar1) # добавляет ключ значение из одного словаря в другой для дальнейшего сравнения с меньшим словарем
    else: 
        # print(f' кто длиннее 2 строка ',slovar2) # длинее оказалась в этот раз 2 строчка
        slovar3.update(slovar2) # или этот если он окажется длинее

    for key, value in slovar3.items():
        if len(slovar3.keys()) != len(slovar1.keys()): # если полученный словарь создавался не из 1 тогда переход на 2 словарь
            if key in slovar1:
                slovar3[key] = int(slovar1[key]) + int(slovar2[key]) # объединяем словари
        else:  # переход на 2 словарь если слияние было не с первым словарем
            if key in slovar2:
                slovar3[key] = int(slovar1[key]) + int(slovar2[key])
    # print(slovar3) # {0: 80, 1: 91, 2: 53, 3: 142, 4: '42'} слияние обоих словарей в один

    for key, value in slovar3.items():
        newslovar[value] = key #  меняем ключ со значением в словаре

    for key, value in newslovar.items():
        newlist.append(key) # перенесли в список только ключ из словаря, значения убрали
    # print(newslovar) # {80: 0, 91: 1, 53: 2, 142: 3, '42': 4} перевернули словарь
    # print(newlist) # [80, 91, 53, 142, '42'] # избавились от значений, оствив только ключ
    return newlist


newlist = slojenie(te1, te2)

# окончательное вычисление
def sborka(newlist):
    num = newlist
    melist = '' 
    for i in range(0, len(num))[::-1]: # переворачиваем список так как должно быть и добавляем все элементы (+, х, x^? = 0)
        if i == 1:
            melist += str(num[i]) + 'x' 
        elif i == 0:
            melist += ' + ' + str(num[i]) + ' = 0'      
        else: 
            melist += str(num[i]) + 'x^' + str(i) + ' + '
    # print(melist) # 42x^4 + 142x^3 + 53x^2 + 91x + 80 = 0 готовый ответ слияния многочленов
    return melist

print(sborka(newlist))
temp = sborka(newlist) 

file_end = temp # создаем файл и передаем значения нашего полинома
with open('polynomial_end.txt', 'w') as data:
    data.write(file_end)


   





























# slovar3 = defaultdict(list)
# for k, v in chain(slovar1.items(), slovar2.items()):
#     slovar3[k].append(v)



# k=set(list(slovar1.keys())+list(slovar2.keys()))
# for i in range(0,100):
#     v1=slovar1.get(i)
#     v2=slovar2.get(i)
  
#     v=int(v1+v2)
#     slovar3[i]=v

 
# print(slovar3)




# slovar3 = {**slovar1, **slovar2}

# slovar3 = slovar1.copy()   # place the dictionary values from x into z
# slovar3.update(slovar2)
# for key, v in slovar3.keys():
#      if key in slovar2.keys():
#         slovar3[v] = slovar3[v] + slovar2[v]