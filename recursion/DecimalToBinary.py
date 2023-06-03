"""
    Convert decimal number to binary number using recursion
"""


def my_convert_dec_to_bi(num: int) -> int:
    assert int(num) == num, "Integers only"
    n = int(num/2)
    if n == 0:
        return num % 2
    else:
        return num % 2 + 10 * my_convert_dec_to_bi(n)


def decimalToBinary(n):
    assert int(n) == n, "The parameter must be an integer only!"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


# print(my_convert_dec_to_bi(13))
print(decimalToBinary(13))
