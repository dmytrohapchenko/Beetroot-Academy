"""
from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    Checks if input string is Palindrome
    -> is_palindrome('mom')
    True

    -> is_palindrome('sassas')
    True

    -> is_palindrome('o')
    True
    pass
"""


def is_palindrome(looking_str: str) -> bool:
    """Returns True if the given word is palindrome"""
    if isinstance(looking_str, int):
        raise ValueError('ValueError: Only strings accepted')

    if len(looking_str) < 2:
        return True

    looking_str = looking_str.lower()
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


print(is_palindrome('mom'))
print(is_palindrome('o'))
