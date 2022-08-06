
def prosm():
    with open("E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt", "r", encoding='utf-8') as input:
        with open("temp.txt", "w", encoding='utf-8') as output:
            output = input.read()
            print(output)
