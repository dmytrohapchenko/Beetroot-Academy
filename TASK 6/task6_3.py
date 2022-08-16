numbers = list(range(1,101))
num_list = []
for i in range(0,len(numbers)):
    if numbers[i]%7==0 and numbers[i]%5!=0:
        num_list.append(numbers[i])
print(num_list)