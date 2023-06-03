"""
    Calculate power of a number using recursion
"""
from typing import Union, Any


# f(n) = num * f(n-1)
def my_power_of_number(num: int, pow: int) -> Union[int, float]:
    assert int(pow) == pow, "The power must be integer"
    if pow > 0:
        return num * my_power_of_number(num, pow - 1)
    elif pow < 0:
        return 1/num * my_power_of_number(num, pow + 1)
    else:
        return 1


def power(base, exp):
    assert int(exp) == exp, "The exponent should be integer"
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp + 1)

    return base * power(base, exp - 1)


print(my_power_of_number(2, -2))
print(power(2, -2))

