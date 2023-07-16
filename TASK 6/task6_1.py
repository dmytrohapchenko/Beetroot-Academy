import random


def main():
    return max([random.randint(1, 9999999999) for i in range(10)])


if __name__ == '__main__':
    print(main())
