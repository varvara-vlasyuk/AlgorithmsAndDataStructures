import collections as co
import queue as q
from multiprocessing import Queue

# DEQUE
my_deque = co.deque()   # doubly linked_list based deque implementation
my_deque.append(1)
my_deque.append(1)
print(my_deque)         # deque([1, 1])
my_deque.pop()
print(my_deque)         # deque([1])
my_deque.append(2)
my_deque.appendleft(3)
print(my_deque)         # deque([3, 1, 2])
my_deque.popleft()
print(my_deque)         # deque([1, 2])
# COUNTER
my_counter = co.Counter(['a', 'a', 'b', 'c', 'c', 'c'])     # dict subclass, works as dict, has overwritten constructor
print(my_counter)       # Counter({'c': 3, 'a': 2, 'b': 1})
print(my_counter.keys())    # dict_keys(['a', 'b', 'c'])
# DEFAULT DICT
my_ddict = co.defaultdict(int)  # dict subclass with overwritten method 'missing' which returns default value instead of error like in custom version
my_ddict['1'] += 1
my_ddict['a'] += 2
print(my_ddict)
# ORDERED DICT
my_ord_dict = co.OrderedDict()      # keeps the order of how keys were appended basing on doubly linked list
my_ord_dict['c'] = 3
my_ord_dict['m'] = 9
my_ord_dict['a'] = 2
print(my_ord_dict)
# NAMED TUPLE
MyTuple = co.namedtuple('TupleName', ['param1', 'param2'])  # creates a class with given parameters
my_tuple = MyTuple(1, 2)
print(f' {my_tuple.param1} {my_tuple.param2}')


# QUEUE MODULE

my_queue = q.Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)
print(f'my_queue.qsize() = {my_queue.qsize()}')
print(my_queue.get())
print(f'my_queue.qsize() = {my_queue.qsize()}')


# MULTIPROCESSING QUEUE MODULE

multi_queue = Queue(maxsize=3)
multi_queue.put(1)
multi_queue.get()