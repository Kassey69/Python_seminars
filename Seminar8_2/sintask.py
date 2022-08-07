

import re
def sintak() :
    f = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'r+', encoding='utf-8')
    txt = f.read()
    # Removes all blank lines # удвлояет все пустые строки
    txt = re.sub(r'\n\s*\n', '\n', txt)
    # # Adds two blanks between all paragraphs № два пробела между всеми абзацами
    txt = re.sub(r'\n', '\n\n\n', txt)
    # # Removes the blank lines from the EOF Удаляет пустые строки из EOF
    # txt = re.sub(r'\n*\Z', '', txt)
    # # Writes to file and closes Записывает в файл и закрывает
    f.write(txt)
    f.close()
    return f