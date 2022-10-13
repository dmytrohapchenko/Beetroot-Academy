"""
Напишіть програму, яка читає послідовність символів і друкує їх у зворотному порядку, використовуючи вашу реалізацію стека.
"""


class Stack:
    def __init__(self, symbols):
        self.symbols = symbols

    def reverse(self):
        return self.symbols[::-1]


test = Stack('Hello')
print(test.reverse())
