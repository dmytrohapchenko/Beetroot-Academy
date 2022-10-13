"""
круглі дужки, фігурна дужка, квадратна дужка
"""


class Stack:
    def __init__(self, symbols):
        self.symbols = symbols

    def balanced(self):
        if self.symbols.count('(') == self.symbols.count(')'):
            if self.symbols.count('{') == self.symbols.count('}'):
                if self.symbols.count('[') == self.symbols.count(']'):
                    return True
        return False


test = Stack('(({{[[}}]]))')
print(test.balanced())
