# Decorator Stacking
def dec_1(fn):
    def inner():
        # first executing the decorator functionality then calling the function
        print("Running decorator 1...")
        return fn()
    return inner

def dec_2(fn):
    def inner():
        # first executing the decorator functionality then calling the function
        print("Running decorator 2...")
        return fn()
    return inner

@dec_1
@dec_2
def fun1():
    print("Running fun1...")
fun1()      # Running decorator 1...\nRunning decorator 2...\nRunning fun1...


def dec_11(fn):
    def inner():
        # First calling the function then executing decorator functionality
        result = fn()
        print("Running dec_11")
        return result
    return inner

def dec_12(fn):
    def inner():
        # First calling the function then executing decorator functionality
        result = fn()
        print("Running dec_12")
        return result
    return inner

@dec_11
@dec_12
def fun2():
    print("Running fun2...")
fun2()      # Running fun2...\nRunning dec_12\nRunning dec_11


# timed decorator
def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print("{0} took {1} seconds".format(fn.__name__, end-start))
        return result
    return inner

# logger decorator
def logger(fn):
    from datetime import datetime, timezone
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0}: called {1}".format(run_dt, fn.__name__))
        return result
    return inner

@logger
@timed
def fact(n):
    from functools import reduce
    return reduce(lambda x, y: x*y, range(1, n+1))
# the above definition is similar to : fact = logger(timed(fact))

print(fact(4))
# fact took 1.7728000000001576e-05 seconds
# 2021-07-03 05:55:22.743822+00:00: called fact
# 24
