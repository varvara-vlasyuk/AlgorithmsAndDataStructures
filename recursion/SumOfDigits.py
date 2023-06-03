"""
    Find the sum of digits of a positive integer number using recursion
"""


def my_recursive_sum(num: int, sum: int = 0) -> int:
    if num > 0:
        sum += num % 10
        sum = my_recursive_sum(round(num/10), sum)
    else:
        return -1

    return sum


def recursive_sum(num):
    assert 0 <= num == int(num), "The number has to be positive"
    if num == 0:
        return 0
    else:
        return num % 10 + recursive_sum(int(num/10))


print(my_recursive_sum(1234))
print(recursive_sum(1234))

