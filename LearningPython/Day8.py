# lambda functions
import random

f = lambda x: x**2
print(f(9))

my_func = lambda x, y=10: x + y
print(my_func(2, 3))  # o/p: 5
my_func(2)  # o/p: 12

func = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(func(1, 'a', 'b', y=100, a=200, b=500))
# output: (1, ('a', 'b'), 100, {'a': 200, 'b': 500})

def sq(x):
    return x**2

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(apply_func(sq, 2))    # OUTPUT: 4
print(apply_func(lambda x, y: x+y, 2, 5))   # OUTPUT: 7
print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5))   # OUTPUT: 15

# Application of lambda: sorting
lst = [2, 4, 1, 3, 8, 5, 6, 7]
print(sorted(lst))
# Note: lst is still the same because sorted() is not inplace sorting

help(sorted)
# Note: 'key' argument(keyword based) is used to specify the type of sorting.
# key points to a function object

print(sorted(lst, key=lambda x: 1/x))   # OUTPUT: [8, 7, 6, 5, 4, 3, 2, 1]
# first change each x to 1/x in lst, then apply sorting
# note: x must not be zero

print(sorted(lst, key=lambda x: -x))    # OUTPUT: [8, 7, 6, 5, 4, 3, 2, 1]
# first change x to -x then apply sorting

# case insensitive sorting
lst = ['c', 'B', 'a', 'D']
print(sorted(lst, key=lambda c: c.upper()))     # OUTPUT: ['a', 'B', 'c', 'D']

# sorting dictionaries based on value
my_dict = {'abc': 500, 'def': 300, 'ghi': 200}
print(sorted(my_dict, key=lambda e: my_dict[e]))    # OUTPUT: ['ghi', 'def', 'abc']

# sorting list of complex numbers
def dist_sq(x):
    return x.real ** 2 + x.imag ** 2

my_comp = [2+2j, 3-1j, 5j, -1+4j, 3+1j]
print(sorted(my_comp, key=dist_sq))     # OUTPUT: [(2+2j), (3-1j), (3+1j), (-1+4j), 5j]

# without dist_sq()
print(sorted(my_comp, key=lambda x: x.real ** 2 + x.imag ** 2))
# OUTPUT: [(2+2j), (3-1j), (3+1j), (-1+4j), 5j]

# randomising the given list
lst = [1, 2, 3, 4, 5, 6, 7]
print(sorted(lst, key=lambda x: random.random()))





