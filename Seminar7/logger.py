import datetime

def log_data(s):
    dt = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    s = 'Дата и время:' + ' ' + dt + '; ' + s + '\n'
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar7\log_file.txt', 'a', encoding='utf-8') as l:
        l.write(s)

