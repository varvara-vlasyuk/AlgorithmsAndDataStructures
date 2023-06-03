"""
Calculate the Fibonacci's nth number
"""


def fibonacci(num: int, meta=None) -> int:
    if meta is None:
        meta = {}
    if num == 1:
        return 0
    if num == 2:
        return 1

    if num not in meta.keys():
        meta[num] = fibonacci(num - 1, meta) + fibonacci(num - 2, meta)

    return meta[num]


print(fibonacci(7))
