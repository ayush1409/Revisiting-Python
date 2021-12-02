# Working with **kwargs
# **kwargs is used to scoop all keyword arguments

def fun1(a, b, **kwargs):
    # a, b are mandatory positional arguments
    print(a, b, kwargs)


fun1(1, 3, x=100, y=200)


# def fun1(a, b, *, **kwargs):  # this is wrong syntax
def fun2(*args, **kwargs):
    print(args, kwargs)


fun2(x=100, y=200)
fun2(1, 2)
fun2(2, 5, x=100, y=500)


def fun3(a, b, *args, x, y=200, **kwargs):
    # a is mandatory positional argument
    # b is optional positional argument
    # args is additional positional argument(if any)
    # x is mandatory keyword argument
    # y is optional keyword argument
    # kwargs is additional keyword argument
    print(a, b, args, x, y, kwargs)


def fun4(a, b, *, x, y=200, **kwargs):
    # a,b are mandatory positional argument
    # * means no additional positional argument are allowed(if passed)
    # Note: we cannot use default positional argument before * as it will create ambiguity
    # x is mandatory keyword argument
    # y is optional keyword argument
    # kwargs is additional keyword argument
    print(a, b, x, y, kwargs)


# Use case: print function
help(print)


# small application: calculate average of min and max
def calc_avg_low_high(*values, print_console=True):
    low = min(values) if len(values) > 0 else 0
    high = max(values) if len(values) > 0 else 0
    avg = (low + high)/2
    if print_console:
        print("high : {0}, low = {1}, average : {2}".format(high, low, avg))


is_debug = True
calc_avg_low_high(1, 2, 3, 4, 5, 6, 7, 8, 9, print_console=is_debug)

