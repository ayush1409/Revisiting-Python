# decorator class
def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called : a = {0}, b = {1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func():
    pass
my_func()   # decorated function called : a = 10, b = 20

# The above decorator can be created with the help of a class(i.e decorator class) as well
class MyClass:      # acts as decorator factory when the instance of this class is called
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):     # returns a decorator
        def inner(*args, **kwargs):
            print("decorated function called : a = {0}, b = {1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func2():
    pass
my_func2()      # decorated function called : a = 10, b = 20
# same as my_func2 = MyClass(10, 20)(my_func2)