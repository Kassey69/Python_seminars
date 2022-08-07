
    

def obiedin():

    f1 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'r', encoding='utf-8')
    f2 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt', 'r', encoding='utf-8')
    # print('content of first file before appending -', f1.read())
    # print('content of second file before appending -', f2.read())
    f1.close()
    f2.close()
    # opening first file in append mode and second file in read mode
    f1 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH2_file.txt', 'a+', encoding='utf-8')
    f2 = open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\sleSH3_file.txt', 'r', encoding='utf-8')
    # appending the contents of the second file to the first file

    f1.write(f2.read() )

    # f1.write(re.sub(r'\n', '\n\n\n'))
    # f1.write(re.sub(r'\n\s*\n', '\n'))
    # f1.write(re.sub(r'\n*\Z', ''))
            

    # relocating the cursor of the files at the beginning
    f1.seek(0)
    f2.seek(0)

    
    # printing the contents of the files after appendng
    # print('content of first file after appending -', f1.read())
    # print('content of second file after appending -', f2.read())
    
    # closing the files
    f1.close()
    f2.close()
    return f1, f2