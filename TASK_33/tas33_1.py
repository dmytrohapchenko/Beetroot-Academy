import random


def bubble(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1 - j):  # '-j' for optimization
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
            continue
    return list

if __name__ == '__main__':
    test_list = [random.randint(1, 100) for _ in range(23)]
    print(bubble(test_list))
