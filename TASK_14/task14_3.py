from functools import wraps


def arg_rules(type_, max_length, contains):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) is not type_:
                    print("Wrong type")
                    return False
                if len(arg) > max_length:
                    print("Very long")
                    return False
                for item in contains:
                    if item not in arg:
                        print("Doesn't contain some of required symbols")
                        return False
            print(func(*args, **kwargs))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
