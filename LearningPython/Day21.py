# Decorators used in memoization (caching)
from functools import lru_cache

def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))      # calls fib(n) for n in [1,10] once for each n, 55
print(fib(10))      # 55 (no further function call fib(n) for already calculated n)

# But there is a problem,that if we have multiple positional and keyword arguments then
# it will become hard as they are not hashable for a key to dictionary
# in functools module we have lru_cache to do this kind of functionality

@ lru_cache()
def fib_cached(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(10))
print(fib_cached(10))
# lru means least recently used
# we can set cache size using maxsize keyword argument(read more in documentation)