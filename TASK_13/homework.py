def digit(number, operator=None):
    if operator is None:
        return number
    return operator(number)

def zero(operator=None): return digit(0, operator)
def one(operator=None): return digit(1, operator)
def two(operator=None): return digit(2, operator)
def three(operator=None): return digit(3, operator)
def four(operator=None): return digit(4, operator)
def five(operator=None): return digit(5, operator)
def six(operator=None): return digit(6, operator)
def seven(operator=None): return digit(7, operator)
def eight(operator=None): return digit(8, operator)
def nine(operator=None): return digit(9, operator)

def plus(second_operand): 
    return lambda first_operand: int(first_operand + second_operand)
def minus(second_operand): 
    return lambda first_operand: int(first_operand - second_operand)
def times(second_operand): 
    return lambda first_operand: int(first_operand * second_operand)
def divided_by(second_operand): 
    return lambda first_operand: int(first_operand / second_operand)
