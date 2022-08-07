from asyncio.streams import FlowControlMixin
import csv
import menu_proverka as mn
import controller as cont

def wef():
    otdel =  {1 :'ПТО',  2 :'Бугалтерия', 3 :'снабжение'}
    doljnost = {1 :'Руководитель',  2 : 'Специалист', 3 :'Инженер'}
    sotrudnik = {}
    count = 0
    redor = []
    i = 0
    cor = 4
    # for i in range(40):
    while cor != 0:
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
        
        # sotrudnik = {v:k for k, v in sotrudnik.items()}
        # print(sotrudnik)
        
        for key,y in  sotrudnik.items() :
            sotr = list(sotrudnik.keys())
    
        sot = ",".join(item for item in sotr)
        otdel1 = ''       
        if count == 1: 
        
            otdel1 = str(f'Идентификатор') + str(' ') + str('Имя: ') + str(sot) + str('; ID отдела: ') + str(1) + str(' ') + str(otdel[1]) \
                +  str('; ID Должности: ') + str(1) +  str(' ') + str(doljnost[1])         
            print(f'Идентификатор Имя: {sot}; ID отдела: {otdel[1]}; ID Должности:{doljnost[1]}')
        if count == 2: 
                otdel2 = str(f'Идентификатор') + str(' ') + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(2) + str(' ') \
                    + str(otdel[2]) +  str('; ID Должности: ') + str(2) + str(' ') + str(doljnost[2])
                print(f'Идентификатор Имя: {sot}; ID отдела: {otdel[2]}; ID Должности:{doljnost[2]}')
        if count == 3: 
                otdel3 = str(f'Идентификатор') + str(' ') + str('Имя: ')+ str(sot) +  str('; ID отдела: ') + str(3) + str(' ') \
                    + str(otdel[3]) +  str('; ID Должности: ') + str(3) + str(' ') + str(doljnost[3])
                print(f'Идентификатор Имя: {sot}; ID отдела: {otdel[3]}; ID Должности:{doljnost[3]}')
         
        with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', 'a+', encoding='utf-8') as file:
            # data = file.read() 
    
            if count == 1 : 
                i +=1 
                file.write(', '.join([otdel1])+ '\n') 
            elif count == 2 : 
                i +=1
                file.write(', '.join([otdel2])+ '\n')
            elif count == 3 :
                i +=1
                file.write(', '.join([otdel3])+ '\n')
            
        inputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', "r", encoding='utf-8')
        outputFile = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', "w", encoding='utf-8')
    

        lines_seen_so_far = set() # будем записывать в файл только уникальные данные
        for x in inputFile:
                if x not in lines_seen_so_far and doljnost[1]  != x \
                    and  doljnost[2]  != x and doljnost[3] != x:
                    
                    outputFile.write(x)
                else:
                    lines_seen_so_far.add(x)  
                
        inputFile.close()
        outputFile.close()
        cor -=1
        print(f' Осталось до выхода в главное меню {cor}, думаю вам хватит, 1 отдел заполянется 1 раз')
    else:
        cont.button_click()   
       
    return sotrudnik














        
      
          
 





