import functools


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def call_int(*args, **kwargs):
            print('Convert to int')
            x = func(*args, **kwargs)
            return int(x)

        return call_int()

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def call_str(*args, **kwargs):
            print('Convert to str')
            x = func(*args, **kwargs)
            return str(x)

        return call_str

    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def call_bool(*args, **kwargs):
            print('Convert to bool')
            x = func(*args, **kwargs)
            return bool(x)

        return call_bool

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def call_float(*args, **kwargs):
            print('Convert to float')
            x = func(*args, **kwargs)
            return float(x)

        return call_float


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
