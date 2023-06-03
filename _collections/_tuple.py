"""
    General information about tuples
"""

# O(1) for creation
my_tuple = 1, 3, 4, 6               # original syntax
my_tuple1 = ('a', 'b', 'c')         # sugar, is recommended to identify tuple easily
my_tuple2 = ('s', )                 # comma is required for interpreter to distinguish simple variables from tuples
my_tuple3 = tuple('abcd')           # ('a', 'b', 'c', 'd') the constructor parameter is iterable
test_dict = {6: 'k', 9: 'o'}
test_tuple = tuple(test_dict)       # (6, 9)
# immutable!!!
# my_tuple[0] = 6     # doesnt work
s = my_tuple.index(3)               # 1
if s in my_tuple:
    print('contains')
# operations
concat = my_tuple + my_tuple2       # (1, 3, 4, 6, 's')
multiply = my_tuple1 * 3            # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
count = multiply.count('a')         # how many times a value is presented in tuple
# min. max, sum, any, all, sorted work as well


