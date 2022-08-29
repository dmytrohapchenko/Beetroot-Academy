def oops():
    print('Oops. There must be some error.')
    raise IndexError


def test_function(arg1, arg2):
    result = arg1
    try:
        result /= arg2
        return f'Result equals to {round(result, 2)}.'
    except:
        oops()


x = test_function(100, 10)
print(x)

print()

x = test_function(100, 0)
print(x)
