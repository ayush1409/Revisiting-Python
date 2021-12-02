# reduce function
from functools import reduce

# our own reduce function
def _reduce(func, iterable):
    result = iterable[0]
    for i in iterable[1:]:
        result = func(result, i)
    return result

print(_reduce(lambda a, b: a+b, [1, 2, 3, 4, 5]))   # 15
print(_reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5]))     # 5
print(_reduce(lambda a, b: a*b, [1, 2, 3, 4, 5]))   # 120

# using inbuilt reduce function
print(reduce(lambda a, b: a+b, [1, 2, 3, 4, 5]))    # 15
print(reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5]))      # 5
print(reduce(lambda a, b: a*b, [1, 2, 3, 4, 5]))    # 120
print(reduce(lambda a, b: a + " " + b, ["python", "is", "awesome"]))    # python is awesome
# There is a join method already exists to do the above operation
print(reduce(lambda a, b: a if a < b else b, "python"))     # h

# some useful inbuilt reduce functions are - min, max, sum, any, all
print(any([0, '', None, 100]))      # True
print(any([0, '', None]))           # False
print(all([0, 10, 20, 30]))         # False
print(all([-1, 10, 20, 30]))        # True
print(sum([1, 2, 3, 4, 5]))         # 15

# Factorial of a number using reduce function
n = int(input("Enter a number: "))
print("Factorial of ", n, " : ", reduce(lambda a, b: a*b, range(1, n+1)))