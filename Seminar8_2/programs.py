from asyncio.streams import FlowControlMixin
import csv
import menu_proverka as mn


def wef():
    otdel =  {1 :'ПТО',  2 :'Бугалтерия', 3 :'снабжение'}
    doljnost = {1 :'Руководитель',  2 : 'Специалист', 3 :'Инженер'}
    sotrudnik = {}
    count = 0
    redor = []
    i = 0
    # for i in range(40):
    while i <= 6:
        count = 0           
        name = input('Введите свое имя ')
        number_otdel = mn.menu_proverka()
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
            print (f" Должность уже занята, выберите другое{sotrudnik}, не прошло {count}") 
        

        sotrudnik = {v:k for k, v in sotrudnik.items()}
        print(sotrudnik)
        
        for key,y in  sotrudnik.items() :
            sotr = list(sotrudnik.keys())
       
        sot = ",".join(item for item in sotr)
        otdel1 = '' 
        
        if count == 1: 
         
             otdel1 = str(i+1) + str('Имя: ') + str(sot) + str('; ID отдела: ') + str(1) + str(' ') + str(otdel[1]) \
                +  str('; ID Должности: ') + str(1) +  str(' ') + str(doljnost[1])         
        
        if count == 2: 
                otdel2 = str(i+1) + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(2) + str(' ') \
                    + str(otdel[2]) +  str('; ID Должности: ') + str(2) + str(' ') + str(doljnost[2])
        if count == 3: 
                otdel3 = str(i+1) + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(3) + str(' ') \
                    + str(otdel[3]) +  str('; ID Должности: ') + str(3) + str(' ') + str(doljnost[3])
      
        
        with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', 'a+', encoding='utf-8') as file:
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
            
            
            outputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', "w", encoding='utf-8')
            inputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', "r", encoding='utf-8')

    
            
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
                        if x == 6: return mn.sotrydniki()
                       
       
    return sotrudnik





