# Applications of *args and **kwargs
import time


# used to return average time to execute fun(*args, **kwargs)
def time_it(fun, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        # Note: fun(args, kwargs) will not pas args as positional and kwargs as keyword arguments
        fun(*args, **kwargs)
    end = time.perf_counter()
    return (end-start)/rep      # returns the average time to execute the given function


print(time_it(print, 1, 2, 3, 4, 5, sep=' - ', end=' ***\n', rep=5))


def compute_powers_1(n, *, start=1, end):
    powers = []
    for i in range(start, end):
        powers.append(n**i)
    return powers


def compute_powers_2(n, *, start=1, end):
    # using list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using generator
    return (n**i for i in range(start, end))


print(time_it(compute_powers_1, 2, start=0, end=2000, rep=5))
print(time_it(compute_powers_2, 2, start=0, end=2000, rep=5))
print(time_it(compute_powers_3, 2, start=0, end=2000, rep=5))






