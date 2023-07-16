def main():
    numbers = [i for i in range(1, 101)]
    num_list = []
    for i in numbers:
        if i % 7 == 0 and i % 5 != 0:
            num_list.append(i)
    return num_list


if __name__ == '__main__':
    print(main())
