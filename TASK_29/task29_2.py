#Task 2

#Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential, binary searches.

def fibonacci(num) -> int:
    n1, n2 = 0, 1
    for i in range(0, num):
        n1, n2 = n2, n1+n2
    return n1

print(fibonacci(10))
assert fibonacci(10) == 55
assert fibonacci(5) == 34