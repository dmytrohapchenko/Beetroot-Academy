list_of_args = []


def take_input():
    input_operator = input(
        'Please, enter a valid operator (+ - * / ):  ') \
        .replace(' ', '')
    input_args = input(
        'Please, enter arguments, separated by comma: ') \
        .replace(' ', '').split(',')
    return input_operator, input_args


def input_checker(input_to_check):
    if type(input_to_check) == int or type(input_to_check) == float:
        list_of_args.append(float(input_to_check))

    elif type(input_to_check) == list or type(input_to_check) == tuple:
        for i in range(len(input_to_check)):

            if '-' in str(input_to_check[i]) or '.' in str(
                    input_to_check[i]) or str(input_to_check[i]).isdecimal():

                if str(input_to_check[i]) \
                        .replace('-', '').isdigit() == False or str(
                    input_to_check[i])\
                        .replace('-', '').isdecimal() == False:
                    continue

                list_of_args.append(float(input_to_check[i]))
    else:
        print('Sorry, you have to enter valid numbers!')


def make_operation(operator, arg1, *args):
    if len(list_of_args) > 0:
        result = arg1
        input_checker(args)
    else:

        input_checker(arg1)
        result = arg1
        input_checker(args)

    if operator == '+':
        for i in list_of_args[1:]:
            result += i
        print(result)

    if operator == '-':
        for i in list_of_args[1:]:
            result -= i
        print(result)

    if operator == '*':
        result = 1
        for i in list_of_args[:]:
            result *= i
        print(result)

    if operator == '/':

        if 0 in list_of_args:
            print('You are not allowed to divide by Zero!')
            quit()
        for i in list_of_args[1:]:
            result /= i

        print(round(result, 2), )

    if operator.strip() not in "+-*/":
        print('Sorry, wrong operator. Try again.')
        quit()


operator_input, input_to_check = take_input()

input_checker(input_to_check)

arg1 = list_of_args[0]
args = list_of_args[1:]

make_operation(operator_input, arg1, args)
