def fio_data():
    name = 'Jeff'
    surname = 'Bezos'
    patronymic = 'Preston'

    def print_fio():
        print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())

    return print_fio()


fio_data()