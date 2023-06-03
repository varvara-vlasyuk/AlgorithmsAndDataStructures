"""
    General information about dictionaries
"""

# based on hash table
my_empty_dict = dict()
my_dict = {'one': 'uno', 'two': 'dos'}
value = my_dict['one']
# O(1)
my_dict['three'] = 'tres'
# O(1)
my_dict.pop('two')              # {'one': 'uno', 'three': 'tres'}
my_dict.popitem()               # pops random pair  {'one': 'uno'}
del my_dict['one']              # {}

my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
copied_dict = my_dict.copy()

new_dict = {}.fromkeys([1, 2, 3], 0)        # {1: 0, 2: 0, 3: 0}
# O(n)
my_dict.get(1)                      # 'one'
my_dict.items()                     # dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])
my_dict.keys()                      # dict_keys([1, 2, 3, 4])
# returns value if the key exists and adds new pair if doesnt
my_dict.setdefault(8, 'eight')      # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 8: 'eight'}
s = my_dict.setdefault(1, 'eight')  # s = 'one'

my_dict.values()                    # dict_values(['one', 'two', 'three', 'four', 'eight'])

my_dict.update({'a': 'A', 'b': 'B'})    # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 8: 'eight', 'a': 'A', 'b': 'B'}
# returns True if all the elements are true
bool_dict = {1: True, 2: True}
b = all(bool_dict.values())             # b = True
bool_dict[3] = False                    # {1: True, 2: True, 3: False}
b = all(bool_dict.values())             # b = False
# returns True if at least one element is true
bool_dict = {1: 1, 2: 0, 3: 1}
b = any(bool_dict.values())             # b = True
# sorting - returns LIST
unsorted = {3: '3', 1: '1', 7: '7', 5: '5'}
sorted_dict = sorted(unsorted)               # [1, 3, 5, 7]


print(sorted)


