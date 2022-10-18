"""
from typing import Optional
def mult(a: int, n: int) -> int:
    This function works only with positive integers

    -> mult(2, 4) == 8
    True

    -> mult(2, 0) == 0
    True

    -> mult(2, -4)
    ValueError("This function works only with positive integers")
"""


def mult(a: int, n: int) -> int:
    """Return the result of a * n"""
    if n < 0:
        raise ValueError("This function works only with positive integers")

    if not isinstance(a, int) or not isinstance(n, int):
        raise TypeError("Accepts only integers")

    if n < 1:
        return 0
    return a + mult(a, n - 1)


print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
print(mult(2, -4))
