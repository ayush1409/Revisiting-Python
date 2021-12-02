# Applications of closures - Part 2

# counting function - functions used to create the closures for a given function
# to help us to count the number of times that functions is being called
def counting_func(fn):
    cnt = 0

    def count(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("{0} is being called {1} times.".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return count

def add(a, b):
    return a+b
def mult(a, b):
    return a*b

counter_add = counting_func(add)
print(counter_add.__closure__)
# (<cell at 0x01441FB8: int object at 0x657FA7A0>, <cell at 0x0145C0E8: function  object at 0x01464100>)
print(counter_add.__code__.co_freevars)     # ('cnt', 'fn')
counter_mult = counting_func(mult)


print(counter_add(2, 5))    # add is being called 1 times.\n7
print(counter_add(6, 9))    # add is being called 2 times.\n15
print(counter_mult(4, 6))   # mult is being called 1 times.\n24
print(counter_mult(3, 2))   # mult is being called 2 times.\n6


# The same application we can built more efficiently
# counters is a dictionary that stores (function name, number of times called) pairs
counter = dict()

def counters(fn, c):
    cnt = 0

    def count(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        c[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return count

# Note that we don't need another function name to create closures
add = counters(add, counter)
mult = counters(mult, counter)
add(2, 5)
add(6, 7)
mult(6, 8)
print(counter)      # {'add': 2, 'mult': 1}


