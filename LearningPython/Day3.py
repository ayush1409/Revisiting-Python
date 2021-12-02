# Working with *args and keyword arguments

def fun1(a, b, *args):
    print(a, b, args)


# Note: args is the packed tuple not a list
fun1(1, 2, 3, 4, 5)
fun1(1, 2, 'abc')


def avg(*args):
    sumElement = sum(args)
    count = len(args)
    return count and sumElement / count  # using short circuiting


print(avg(1, 2, 3, 4, 5, 6, 7, 8))


def fun2(a, b, c):
    print(a, b, c)


l = [3, 2, 1]
fun2(*l)


# Note: *args is used to scoop all the positional arguments, * is used to stop taking more positional arguments
# Note: Once we use *args, next arguments can only be keyword arguments
# Note: the order of keyword argument in the callee does not matter as we need to pass the name as well

# putting all together
def fun1(a, b=1, *args, d, e=True):
    # 'a' mandatory positional argument
    # 'b' optional positional argument
    # 'args' additional positional arguments(if any)
    # 'd' mandatory keyword argument
    # 'e' optional keyword argument
    print(a, b, args, d, e)


fun1(1, 'abc', 4, 'efg', d=15)


def fun2(a, b=1, *, d, e=True):
    # 'a' mandatory positional argument
    # 'b' optional positional argument
    # '*' No more additional positional arguments allowed(if any)
    # 'd' mandatory keyword argument
    # 'e' optional keyword argument
    print(a, b, d, e)


fun2(1, 7, e=False, d='abc')


