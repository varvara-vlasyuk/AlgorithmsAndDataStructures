"""
    Find GCD of two numbers using recursion
"""


# Euclidian algorithm
def my_gcd(num1: int, num2: int) -> int:
    assert int(num1) == num1 and int(num2) == num2, "Numbers must be integer"
    if num2 == 0:
        return abs(num1)
    else:
        return my_gcd(num2, num1 % num2)


def gcd(a,b):
    assert int(a) == a and int(b) == b, "Numbers must be integer"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return gcd(b, a%b)


# print(my_gcd(-18, -48))
print(gcd(-18, -48))




