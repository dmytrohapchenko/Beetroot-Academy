import random

numbers_1 = list()
numbers_2 = list()
numbers_3 = []
for i in range(10):
    numbers_1.append(random.randint(1,11))
    numbers_2.append(random.randint(1,11))
for j in range(len(numbers_1)):
    numbers_3.append(numbers_1[j])
    numbers_3.append(numbers_2[j])

print(list(set(numbers_3)))
