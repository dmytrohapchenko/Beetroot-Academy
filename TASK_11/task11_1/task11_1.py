with open('file.txt', 'w') as txt_file:
    txt_file.write('Hello World!\n')
with open('file.txt') as txt_file:
    print(txt_file.read())
