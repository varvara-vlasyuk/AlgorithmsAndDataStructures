"""
    General information about lists
"""


my_empty_list = []
my_nested_list = [1, '2', ['s', 't']]
my_list = [1, 'str', 2.5]
# O(n)
my_list.insert(1, 'new')        # [1, 'new', 'str', 2.5]
# O(n)
my_list.append(33)              # [1, 'new', 'str', 2.5, 33]
# O(m)
new_list = [11, 2, 14]
my_list.extend(new_list)        # [1, 'new', 'str', 2.5, 33, 11, 2, 14]
# slicing
print(my_list[0:2])             # == my_list[:2] == [1, 'new']
my_list[0:2] = ['x', 'y']       # ['x', 'y', 'str', 2.5, 33, 11, 2, 14]
# pops element and returns it
my_list.pop()                   # the last element : ['x', 'y', 'str', 2.5, 33, 11, 2]
my_list.pop(1)                  # the element by index : ['x', 'str', 2.5, 33, 11, 2]
# deletes element by index
del my_list[2]                  # ['x', 'str', 33, 11, 2]
del my_list[0:2]                # [33, 11, 2]
# remove by value
my_list.remove(11)              # [33, 2]
# get index by value
my_list.index(2)
# in operator
if 2 in my_list:
    print('contains')
# concatenation
concat_list = my_list + new_list    # [33, 2, 11, 2, 14]
# repeat values
repeated_list = my_list * 2         # [33, 2, 33, 2]
# aggregations
print(min(my_list), max(my_list), sum(my_list))  # 2 33 35
#  string to list and back
my_str = 'sting'
my_list_from_str = list(my_str)         # ['s', 't', 'i', 'n', 'g']
my_list_from_str = my_str.split('i')    # the default delimiter is space # ['st', 'ng']
my_str = ','.join(my_list_from_str)     # st,ng
# copying the list
orig = my_list[:]
# sorting | O(n log n) Timsort algorithm(combination of mergesort and insertion sort)
new_list = sorted(my_list)              # new_list = [2, 33] my_list = [33, 2]
my_list.sort()                          # my_list = [2, 33]
# slicing
a=[1, 2, 3, 4, 5]               # my_array[start:stop:step]  every nth element from the array, where n is the step size
print(a[3:0:-1])                # [4, 3, 2]

