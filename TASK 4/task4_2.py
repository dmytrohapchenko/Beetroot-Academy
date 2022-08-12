num = input()
counter = 0
if len(num) == 10:
    for i in range(len(num)):
        if num[i] in '0123456789':
            counter += 1
    if counter == 10:
        print('Everything is ok!')
    else:
        print('Wrong phone number!')
else:
    print('Wrong phone number!')