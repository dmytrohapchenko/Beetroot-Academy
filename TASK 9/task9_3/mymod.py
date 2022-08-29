def count_lines(file=open('text.txt')):
    return f'Number of lines:{len(file.readlines())}'


def count_chars(file=open('text.txt')):
    return f'Number of characters:{len(file.read())}'


def test():
    return f'{count_lines()}\n{count_chars()}'
