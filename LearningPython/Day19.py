# Applications of Decorators - Part 1 (timed decorator)
# timed decorator is used to add functionality that tells how much time is taken by a function to run

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(x) for x in args]
        kwargs_ = ["{0}={1}".format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print("{0}({1}) took {2:.6f}s to run.".format(fn.__name__, args_str, elapsed))
        return result
    return inner

# recursive fibonacci
def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# Decorating helper_fib_rec so that not to print time in each call
@timed
def helper_fib_rec(n):
    return fib_rec(n)

helper_fib_rec(6)       # helper_fib_rec(6) took 0.000007s to run.
helper_fib_rec(12)      # helper_fib_rec(12) took 0.000083s to run.
helper_fib_rec(20)      # helper_fib_rec(20) took 0.002627s to run.
helper_fib_rec(22)      # helper_fib_rec(22) took 0.007739s to run.

# looped fibonacci
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_1 + fib_2, fib_1
    return fib_1

fib_loop(6)     # fib_loop(6) took 0.000005s to run.
fib_loop(12)    # fib_loop(12) took 0.000002s to run.
fib_loop(20)    # fib_loop(20) took 0.000006s to run.
fib_loop(22)    # fib_loop(22) took 0.000003s to run.

# Note: If we want to run the timed decorated function multiple times,
# we can use parameterized version of timed decorator and pass the the number of repetetion as argument
