from functools import wraps


def logger(func):
    print(f"Decorating function '{func.__name__}'")

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} parameters: {args}')

    return wrapper()


@logger
def summing(a, b):
    return a + b




