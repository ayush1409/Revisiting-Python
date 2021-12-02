# Working with partial functions
# partial is used when we need to reduce the number of parameters in an existing function
from functools import partial

def func(a, b, c):
    print(a, b, c)

fun1 = lambda b, c: func(10, b, c)
fun1(20, 30)            # 10 20 30
print(type(fun1))       # <class 'function'>

# using the inbuilt partial function
fun2 = partial(func, 10)        # a will get 10 (first positional)
fun2(20, 30)        # 10 20 30

fun3 = partial(func, 10, 20)    # a = 10, b = 20
fun3(30)            # 10 20 30

# handling multiple arguments
def func1(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

# without partial
fun4 = lambda b, *args, k2, **kwargs: func1(10, b, *args, k1='a', k2=k2, **kwargs)
fun4(20, 30, 40, k2='b', k3=100, k4=200)    # 10 20 (30, 40) a b {'k3': 100, 'k4': 200}

# with partial
fun5 = partial(func1, 10, k1='a')
fun5(20, 30, 40, k2='b', k3=100, k4=200)    # 10 20 (30, 40) a b {'k3': 100, 'k4': 200}

def power(base, exponent):
    return base ** exponent

sq = partial(power, exponent=2)
cu = partial(power, exponent=3)
print(sq(5))        # 25
print(cu(5))        # 125
# Note that the exponent value is not fixed i.e
print(sq(5, exponent=3))    # we overwrote value of exponent

# Application of partial
# sorting given list of coordinates based on their distance from origin
def dis(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

origin = (0, 0)
points = [(1, 2), (-1, 2), (0, 4), (3, 0), (0, 0), (10, 1)]
print(sorted(points, key=partial(dis, origin))) # [(0, 0), (1, 2), (-1, 2), (3, 0), (0, 4), (10, 1)]
print(sorted(points, key=lambda a: a[0]**2+a[1]**2))    # [(0, 0), (1, 2), (-1, 2), (3, 0), (0, 4), (10, 1)]

