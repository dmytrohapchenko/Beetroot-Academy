def function():
    while True:  # to re-enter a and b
        try:
            a, b = input('Please enter a and b, separated by comma: ') \
                .replace(' ', '').split(',')
            a = int(a)
            b = int(b)
            return f'"a" squared and divided by "0" equals to: {a ** 2 / b}'
        except ZeroDivisionError:
            print('You are not supposed to divide by Zero. Try again: ')
            continue
        except ValueError:
            print('Please enter TWO valid numbers. Try again: ')
            continue
        except:
            print("Hm or i'm a fool or skis don't go. Try again: ")
            continue


x = function()
print(x)
