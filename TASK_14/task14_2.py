from functools import wraps


def censorship(some_list=["pepsi", "BMW"]):
    def decorator(func):
        print(f'Decorating function "{func.__name__}"...')

        @wraps(func)
        def wrap(*args, **kwargs):
            decorated_str = func(*args, **kwargs)
            for word in some_list:
                decorated_str = decorated_str.replace(word, "*")
            print(decorated_str)
            return decorated_str

        return wrap

    return decorator


@censorship()
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")
