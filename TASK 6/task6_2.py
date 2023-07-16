import random

def main():
    l_list1 = [random.randint(1, 11) for i in range(10)]
    l_list2 = [random.randint(1, 11) for i in range(10)]
    l_list3 = []
    for i in range(len(l_list1)):
        l_list3.append(l_list1[i])
        l_list3.append(l_list2[i])
    return list(set(l_list3))


if __name__ == '__main__':
    print(main())
