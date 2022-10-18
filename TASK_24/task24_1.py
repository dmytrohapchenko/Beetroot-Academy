"""
from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    Returns  x ^ exp

    -> to_power(2, 3) == 8
    True

    -> to_power(3.5, 2) == 12.25
    True

    -> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    pass
"""
from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """Returns  x ^ exp"""
    if exp < 0:
        raise ValueError('ValueError: This function works only with exp > 0.')

    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)


print(to_power(2, 3) == 8)
print(to_power(3.5, 2) == 12.25)
print(to_power(2, -1))
