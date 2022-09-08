def variables():
    a = 10
    b = 20

    def inner_variable():
        c = 30

    return inner_variable()


print(
    f"Function name '{variables.__name__}' has "
    f"{variables.__code__.co_nlocals} variables inside.")
