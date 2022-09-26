def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


data = [2, 5, 3, 4, 1, 5]

for i, value in with_index(data, 1):
    print(i, value)
