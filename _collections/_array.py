"""
    General information about arrays
"""
# import array
from array import *
# https://wiki.python.org/moin/TimeComplexity

# time complexity O(1) | space complexity O(n)
arr1 = array('i', [1, 2, 3])
arr2 = array('i', [8, 9])
# typecodes: b B u h H i I l L q Q f d

# time complexity O(n) | space complexity O(1)
arr1.insert(2, 0)   # insert 0 to the 2nd position ->  [1, 2, 0, 3]
# time complexity O(n) | space complexity O(n)
arr1.index(2)       # returns index of a given value
# time complexity O(n) | space complexity O(n)
arr1.remove(2)      # removes an element by value
# time complexity O(1)
arr1.append(4)      # adds new element to the end of array
# time complexity O(n)
arr1.extend(arr2)   # extends the array with elements of another array
# time complexity O(n)
list1 = [20, 21]
arr1.fromlist(list1)
# time complexity O(1)
arr1.pop()          # pops the last element
# time complexity O(logn)
arr1.reverse()
#
arr1.buffer_info()  # returns a tuple (address, length) of the buffer used to hold array’s contents
#
arr1.count(2)       # returns the number of occurrences of a value
# DEPRECATED as well as fromstring()
str_var = arr1.tostring()
#
list_var = arr1.tolist()
# slicing
print(arr1[2:])







print(arr1)
