class Stack:
    def __init__(self, sentence):
        self.sentence = sentence.lower()

    def get_from_stack(self, symbol):
        if symbol in self.sentence:
            return symbol
        raise ValueError(f'{symbol} - was not found')


test = Stack('Hello')
print(test.get_from_stack('g'))

