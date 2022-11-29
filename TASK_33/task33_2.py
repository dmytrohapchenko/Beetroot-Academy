import random


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        # left_half = array[:mid]
        # right_half = array[mid:]
        left_half = [array[i] for i in range(0, mid)]
        right_half = [array[i] for i in range(mid, len(array))]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
    return array


if __name__ == '__main__':
    test_list = [random.randint(1, 100) for _ in range(23)]
    print(merge_sort(test_list))