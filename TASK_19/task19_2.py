def in_range(start, end, step=1):
    l_list = []
    while start < end:
        l_list.append(start)
        start += step
    return l_list


print(in_range(1, 10, 2))
