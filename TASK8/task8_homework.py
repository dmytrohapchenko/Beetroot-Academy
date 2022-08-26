import time

symbol = ('---', '\\\\\\', '|||', '///')


def painter():
    while True:
        for i in range(len(symbol)):
            print(symbol[i], end='')
            time.sleep(0.25)
            print('\r', end='')


painter()
