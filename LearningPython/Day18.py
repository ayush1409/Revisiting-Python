# Working with Decorators
from functools import wraps

# Decorator: Creating closures of the same function name
def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("Function {0} has ran {1} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a+b

# decorating means
add = counter(add)
print(add(3, 4))    # Function add has ran 1 times\n7
print(add(7, 9))    # Function add has ran 2 times\n16
print(help(add))    # Help on function inner in module __main__:\n\ninner(*args, **kwargs)
# Note: we don't have any information about previous add function

# decorating using @ symbol
@counter
def mult(a, b):
    return a*b
print(mult(2, 9))   # Function mult has ran 1 times\n18
print(mult(3, 5))   # Function mult has ran 2 times\n15


# How to work with function introspection ?
# we have a problem, after creating closure for a function say fn, we lost the signature of fn
# It has now the signature as inner(*args, **kwargs)
# To avoid this problem, we use a parameterized decorator wraps on the inner function

def add(a: 'int', b: int, c=0):
    return a + b + c

def counter(fn):
    cnt = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("Function {0} has ran {1} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    # we can also do(instead of @wraps)-
    # inner = wraps(fn)(inner)
    return inner

help(add)   # Help on function add in module __main__:\n\nadd(a: 'int', b: int, c=0)
# Note: after decorating add(), it still has the same signature