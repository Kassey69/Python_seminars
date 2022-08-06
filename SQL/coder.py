from asyncio.streams import FlowControlMixin
import csv



def menu_proverka():
    x = input('Выберите номер отдела (1)ПТО (2)Бугалтерия (3)Cнабжение (4)Выход в главное меню\nВвод: ')
    while True:
            try:
             
                    x = int(x)
                 
                    if x < 1 or x > 6: # тут можно ввести три числа 2 3 и 4 которое понадобится для цикла while и выхода
                
                        x = input('Введите корректное число\n')  
                    
                    else:
                        break

            except ValueError: 
                x = input("Вы ввели не число. Повторите ввод\n")
    
    return x



# with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\sle_file.txt', 'a+', encoding='utf-8') as file:
#      file.write(', '.join([name, tel, comment]) + '\n')

# def user_data(): 
def wef():
    otdel =  {1 :'ПТО',  2 :'Бугалтерия', 3 :'снабжение'}
    doljnost = {1 :'Руководитель',  2 : 'Специалист', 3 :'Инженер'}
    # otdel =  [1, 'ПТО',  2, 'Бугалтерия', 3, 'снабжение']
    # doljnost = [1, 'Руководитель',  2,  'Специалист', 3, 'Инженер']
    sotrudnik = {}
    count = 0
    redor = []
    i = 0
    # for i in range(40):
    while i <= 6:
        count = 0 
        
                
        name = input('Введите свое имя ')

        number_otdel = menu_proverka()

        number_otdel = str(number_otdel)
        sotrudnik = { name:number_otdel}  

        print(redor)
        if number_otdel not in redor  and '1' in number_otdel: # нельзя ввести повторно число
            redor.append(number_otdel)   # если 1 мы выбираем в числе
            count += 1 
            print(sotrudnik,count)        
            
        elif number_otdel not in redor and '2' in number_otdel: 
            redor.append(number_otdel)  # если 2 мы выбираем в числе
            count += 2
            print(sotrudnik,count)
          
        elif number_otdel not in redor and '3' in number_otdel: 
            redor.append(number_otdel) # если 1 мы выбираем в числе
            count += 3
            print(sotrudnik,count)
        else: 
            print (f" Должность уже занята, выберите другое{sotrudnik,count}") 
        

        # sotrudnik = {v:k for k, v in sotrudnik.items()}
        # print(sotrudnik)

        
        for key,y in  sotrudnik.items() :
            sotr = list(sotrudnik.keys())
       
        sot = ",".join(item for item in sotr)
        otdel1 = '' 
        
        if count == 1: # otdel =  {1 :'ПТО',  2 :'Бугалтерия', 3 :'снабжение'}
                    # doljnost = [1, 'Руководитель',  2,  'Специалист', 3, 'Инженер']
               
            # otdel1 = str(i) + str(sot) + str(otdel[0]) + str(otdel[1]) + str(doljnost[0]) +str(doljnost[1]) 
            # otdel1 = str(sotrudnik) + str(otdel[0]) + str(otdel[1]) + str(doljnost[0]) +str(doljnost[1]) 
             otdel1 = str(i+1) + str('Имя: ') + str(sot) + str('; ID отдела: ') + str(1) + str(' ') + str(otdel[1]) \
                +  str('; ID Должности: ') + str(1) +  str(' ') + str(doljnost[1])
            #  + str(otdel[1]) + str(doljnost[0]) + str(doljnost[1]) 
        # print(f'{i+1}, {sot}, {otdel[0]} {otdel[1]}, {doljnost[0]} {doljnost[1]}')
        
        if count == 2: # print(f'{i+1}, {sotrudnik}, {otdel[2]} {otdel[3]}, {doljnost[2]} {doljnost[3]}')
                otdel2 = str(i+1) + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(2) + str(' ') \
                    + str(otdel[2]) +  str('; ID Должности: ') + str(2) + str(' ') + str(doljnost[2])
        if count == 3: # print(f'{i+1}, {sotrudnik}, {otdel[4]} {otdel[5]}, {doljnost[4]} {doljnost[5]}')
                otdel3 = str(i+1) + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(3) + str(' ') \
                    + str(otdel[3]) +  str('; ID Должности: ') + str(3) + str(' ') + str(doljnost[3])
      
        # with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\sleSH_file.txt', 'a+', encoding='utf-8') as file:
        #     file.write(', '.join([str(i+1), str(sot), str(otdel[0]), str(otdel[1]), str(doljnost[0]), str(doljnost[1])]) + '\n')
        
        with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\sleSH_file.txt', 'a+', encoding='utf-8') as file:
            data = file.read()
            data = set()
    
            if count == 1 and doljnost[1] not in data and otdel[1] not in data: 
                i +=1 
                file.write(', '.join([otdel1])+ '\n') 
            elif count == 2 and doljnost[2] not in data and otdel[2] not in data: 
                i +=1
                file.write(', '.join([otdel2])+ '\n')
            elif count == 3 and doljnost[3] not in data and otdel[3] not in data:
                i +=1
                file.write(', '.join([otdel3])+ '\n')
            
            
            outputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\sleSH2_file.txt', "w", encoding='utf-8')
            inputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\sleSH_file.txt', "r", encoding='utf-8')

            # Метод считывает и возвращает считанные данные с файла file_name
            # with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\sleSH_file.txt', 'r', encoding='utf-8') as file:
            #     data = file.read()
            #     if doljnost[1] not in data 
            # print(data)
            
            lines_seen_so_far = set() # будем записывать в файл только уникальные данные
            for x in inputFile:
                if x not in lines_seen_so_far and doljnost[1] !=x and \
                     doljnost[2] != x and doljnost[3] != x:
                    outputFile.write(x)
                    lines_seen_so_far.add(x)  
                   
            inputFile.close()
            outputFile.close()
            q = (input ('Вы можете завершить нажав на 6')) 
            while True:
                try:
                    x = int(input('Выберите варианты \n (1)добавить сотрудника (2)удалить сотрудника; (3)Изменить данные (4) Импорт БД (5) Экспорт БД (6)Выход из программы\nВвод: '))
                    while x < 1 or x > 7:
                        x = int(input('Введите корректное число')   ) 
                except ValueError: print("Вы ввели не число. Повторите ввод")
                else:
                    while x != 6:
                        if x == 6: return sotrydniki()
                       

                #  file.write(', '.join([otdel1])+ '\n') or  file.write(', '.join([otdel2])+ '\n') or  file.write(', '.join([otdel3])+ '\n')
    return sotrudnik

# print(f'1{sotrudnik} {otdel[0]} {doljnost[0]}')

def sotrydniki():
    while True:
        try:
            x = int(input('Выберите варианты \n (1)добавить сотрудника (2)удалить сотрудника; (3)Изменить данные (4) Импорт БД (5) Экспорт БД (6)Выход из программы\nВвод: '))
            while x < 1 or x > 6:
                x = int(input('Введите корректное число')   ) 
        except ValueError: print("Вы ввели не число. Повторите ввод")
        else:
            while x != 6:
                if x == 1: 
                    print('добавить сотрудника')
                    return wef() 
                elif x == 2: 
                    print('удалить сотрудника')
                    return 
                elif x == 3: 
                    print('Изменить данные')
                    return 
                elif x == 4: 
                    print('Импорт БД')
                    return 
                elif x == 5: 
                    print('Экспорт БД')
                    return 
            else: print ('выход из программы') 
            break                                     
sotrydniki()


