import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1,9999999999))
print(max(numbers))