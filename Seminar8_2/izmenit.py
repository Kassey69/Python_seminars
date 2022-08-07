import os
import prosmotr as pr
import proverka_izmenen as prover
import re
import del_syroki as dl
import controller as contr
import soitie_izmenenii as so
import sintask as sin
import element_smeba2 as elim

def izm():
    print(pr.prosm())
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'r', encoding='utf-8') as file:
        with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w",encoding='utf-8') as dexter:
           # with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееempl.txt", "a+",encoding='utf-8') as links:
             
                x  =  prover.menu_proverka_izm()
                x = str(x)
                x = ''.join(x)
                global b
                b = x
            
                for line in file:       # тут идет выбор какой элемент изменять
                    # if substring contain in a line then don't write it
                    if x in line.strip("\n"):
                        dexter.write(line)
   
    os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt')
    print(pr.prosm())   # переписал изменяемый файл отдельно     
    elim.izmin()  

    data = []
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt', 'r', encoding='utf-8') as files:  
        with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w",encoding='utf-8') as dexters:
            data = files.read().split()
            red = []
            slovar1 = {i : data[i] for i in range(len(data))} 
            slovar1[2] = input('Ведите новое имя')
            # print(slovar1)
            # print(slovar1[2]) # находим файл который будем менть словарем

            for i , y in slovar1.items(): # всекгда должен быть под with внутри
                red.append(y) # переводим из словаря в список          
     
            for i in red:      
                    #     # if x not in i.strip("\n"):               
                dexters.write(', '.join([i])+ ' ')       
    os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt')
    print(pr.prosm())  # перенесли в 3 файл отдельный разобранный который  нужно добавить м изменениями нашими
    files.close()

    so.obiedin()
    # sin.sintak()
    contr.button_click()















    #dl.delet() # тот элемент которыймы будем заменять надо удалить перед заменой  
    # переносим содержимое из одного в другой

    # f1 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'r', encoding='utf-8')
    # f2 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt', 'r', encoding='utf-8')
    # # print('content of first file before appending -', f1.read())
    # # print('content of second file before appending -', f2.read())
    # f1.close()
    # f2.close()
    # # opening first file in append mode and second file in read mode
    # f1 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'a+', encoding='utf-8')
    # f2 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt', 'r', encoding='utf-8')
    # # appending the contents of the second file to the first file

    # f1.write(f2.read() + '\n')

    # # f1.write(re.sub(r'\n', '\n\n\n'))
    # # f1.write(re.sub(r'\n\s*\n', '\n'))
    # # f1.write(re.sub(r'\n*\Z', ''))
            

    # # relocating the cursor of the files at the beginning
    # f1.seek(0)
    # f2.seek(0)

    
    # # printing the contents of the files after appendng
    # # print('content of first file after appending -', f1.read())
    # # print('content of second file after appending -', f2.read())
    
    # # closing the files
    # f1.close()
    # f2.close()

   
    






    # Reads from file
    # f = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'r+', encoding='utf-8')
    # txt = f.read()
    # # Removes all blank lines # удвлояет все пустые строки
    # # txt = re.sub(r'\n\s*\n', '\n', txt)
    # # # Adds two blanks between all paragraphs № два пробела между всеми абзацами
    # txt = re.sub(r'\n', '\n\n\n', txt)
    # # # Removes the blank lines from the EOF Удаляет пустые строки из EOF
    # # txt = re.sub(r'\n*\Z', '', txt)
    # # # Writes to file and closes Записывает в файл и закрывает
    # f.write(txt)
    # f.close()
   












# def izm():
#     print(pr.prosm())

#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', \
#             'r', encoding='utf-8') as file:
#         with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w",\
#             encoding='utf-8') as dexter:

            
#             x  =  prover.menu_proverka_izm()
#             x = str(x)
#             x = ''.join(x)
            

#             for line in file:
#                 # if substring contain in a line then don't write it
#                 if x in line.strip("\n"):
#                     dexter.write(line)
#     os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt')


    # print(pr.prosm())
    # data = []
    # with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', \
    #         'r', encoding='utf-8') as files:
       
    #     with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w",\
    #         encoding='utf-8') as dexters:
    #         data = files.read().split()
    #         red = []
    #         slovar1 = {i : data[i] for i in range(len(data))} 
    #         slovar1[2] = input('Ведите новое имя')
    #         print(slovar1)
    #         print(slovar1[2])

    #         for i , y in slovar1.items(): # всекгда должен быть под with внутри
    #             red.append(y)
            
    #         print(red)

    #     # x = prover.menu_proverka_izm()
    #     # x = str(x)
    #     # x = ''.join(x)

    #         for i in red:      
    #             #     # if x not in i.strip("\n"):
                  
    #             dexters.write(', '.join([i])+ ' ') 
           
    # # with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', 'a+', encoding='utf-8') as file:
    # #         # data = file.read()     
    # os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt')
    # print(pr.prosm())  
    # files.close()
    # return i






















# def delet():

#     print(pr.prosm())
         
#     with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt", "r", encoding='utf-8') as input:
#         with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w", encoding='utf-8') as output:
          
          
#             x  =  prov.menu_proverka()
#             x = str(x)
#             x = ''.join(x)
           

#             for line in input:
#                 # if substring contain in a line then don't write it
#                 if x not in line.strip("\n"):
#                     output.write(line)
#     # replace file with original name
#     os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt')

#     print(pr.prosm())
#     return line




        # for i in data:
          
        #     ret.append([str(data) for data in i.split()])
        # print(ret)


# ' '.join(data)
# list(str(ret).replace(' ',''))
# str(ret).replace(' ','')
# print(ret)
# count = 0
# l = ''
# for i in range(len(ret)-1): 
#     if ret[i] == ret[i+1]:
#         count +=1
#     else: 
#         l += str(count) + str(ret[i])
#         count = 1
# l = str(l) + str(count) + str(ret[-1])                                                    
# print( l)
# import unicodedata



# n = list(str(n).replace('.',''))
    #  for line in file:
    #         data.append([list(map(str, x)) for x in line.split()])




    # data = []
    # with open("data.txt") as f:
    #     for line in f:
    #         data.append([float(x) for x in line.split()])




# def change_data_sotrydnik(new_sotrydnik_data):
#     name = new_sotrydnik_data
#     list_data_sotrydnik = []
#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', \
#         'r', encoding='utf-8') as file:
      
#         data = file.read()
#         count = 0
#         for row in file:
#             if count > 0:
#                 try:
#                     row = row.replace('\n', '')
#                     data_sotrydnik = row.split(';')
#                     if data_sotrydnik[0] not in '':
#                         list_data_sotrydnik.append(data_sotrydnik)
#                 except ValueError:
#                     continue
#             count += 1
#     for i in list_data_sotrydnik:
#         if i[0] == name:
#            i[0] = name

#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt', \
#         'w', encoding='utf-8') as file:
#         data = file.read()
#         data = file.read.row([name])
#         for i in list_data_sotrydnik:
#                 data = file.read.readrow([i[0]])
#     return list_data_sotrydnik
# change_data_sotrydnik(data)


# with open('filename.txt', 'r') as f1, open('filename1.txt', 'w') as f2:
#     lines = f1.readlines()

#     for line in lines:
#         line = line.strip()
#         if line == 'искомая строка':
#             f2.write('новая строка\n')
#         else:
#             f2.write(line)