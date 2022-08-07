import fileinput
import os
import prosmotr as pr
import menu as menu
import del_simbol as de
import proverka_del as prov
import controller as contr

def delet():

    print(pr.prosm())
         
    with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt", "r", \
        encoding='utf-8') as input:
        with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt", "w",\
             encoding='utf-8') as output:
          
          
            x  =  prov.menu_proverka()
            x = str(x)
            x = ''.join(x)
           

            for line in input:
                # if substring contain in a line then don't write it
                if x not in line.strip("\n"): # мы пропускаем ее и она не попадает в список потому что сохраняем сразу
                    output.write(line)
    os.replace("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\ееemp.txt",  'E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt')

    print(pr.prosm())
    contr.button_click()
    return line

    

    # with fileinput.FileInput('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt',  \
    #     inplace=True, backup='.bak') as file:
    #     for line in file:
    #         if not line.startswith('1Имя: Владимир'): 
    #             print(line, end='') # keep line (stdout is redirected to the file)
    # os.unlink('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH_file.txt' + '.bak') 
    # return file