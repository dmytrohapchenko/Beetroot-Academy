#Task 1

#Implement binary search using recursion.

def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 7, 1, 9))