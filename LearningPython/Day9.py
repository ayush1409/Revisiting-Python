# Functions introspection
import inspect
from inspect import isfunction, ismethod, isroutine


# without inspect module
# dir(func) is used  to list all the attributes of function object
def my_func(a: int,
            b: 'int > 0',
            *args: 'additional positional arguments',
            kw1: 'first mandatory keyword argument',
            kw2: 'second mandatory keyword argument',
            **kwargs: 'additional keyword arguments') -> 'a useless value':
    """do something"""
    pass


print(my_func.__annotations__)
my_func.new_attr = 'adding new attribute to my_func'  # use dir(my_func) to see list of all attributes
print(dir(my_func))

# Function introspection using inspect module (much easier)
for param in inspect.signature(my_func).parameters.values():
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
# Use dir(inspect.signature(my_func) to see the different attributes that can be used in function introspection


class SampleClass:
    def my_func(self):
        pass
s_obj = SampleClass()

# functions are defined using def i.e not bounded by any object
# methods are bounded by an object of a class
print(isfunction(my_func))  # OUTPUT: True
print(isroutine(my_func))  # OUTPUT: True
print(ismethod(my_func))    # OUTPUT: False

print(isfunction(s_obj.my_func))    # OUTPUT: False
print(isroutine(s_obj.my_func))  # OUTPUT: True
print(ismethod(s_obj.my_func))  # OUTPUT: True

print(isfunction(SampleClass.my_func))    # OUTPUT: True
print(isroutine(SampleClass.my_func))  # OUTPUT: True
print(ismethod(SampleClass.my_func))  # OUTPUT: False


# how to get source code of a function ?
print(inspect.getsource(my_func))   # prints the complete code in function on terminal
