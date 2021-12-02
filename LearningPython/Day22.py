from functools import reduce

# Parameterized decorators
def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        result = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end-start)
        print("{0} took {1} seconds".format(fn.__name__, total_elapsed/10))
        return result
    return inner

# The problem with the above code is we hardcoded value of number of reps = 10
# we need to optimze the approach by passing the different rep count to decorator
# The nested closure is used to create a decorator factor, the outer function returns additional parameter
# and returns a decorator (not a closure)

def timed_with_reps(reps=10):  # represents a decorator factory, which returns a decorator
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            result = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, *kwargs)
                end = perf_counter()
                total_elapsed += (end-start)
            print("{} took {}".format(fn.__name__, total_elapsed/reps))
            return result
        return inner
    return dec

@timed_with_reps(reps=20)
def fact(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
# above definition is same as fact = timed_with_reps(10)(fact)

print(fact(5))      # fact took 2.0761499999997353e-06\n120


