# working with operator module
import operator
from functools import reduce
# print(dir(operator))    # use this to see all the functionality present inside operator module
# some common functions under operator are - add, mul, lt, is_ and so on

# previously
n = 5
print(reduce(lambda a, b: a*b, range(1, n+1)))      # 120
# now
print(reduce(operator.mul, range(1, n+1)))          # 120

# itemgetter() and getitem()
# itemgetter() is used to get items from multiple(or one) index position
lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
f1 = operator.itemgetter(5)         # f is a callable to get item at index 5
f2 = operator.itemgetter(1, 3, 5)   # f is a callable to get items at index 1,3 and 5
print(f1(lst))      # 4 of int type
print(f2(lst))      # (8, 6, 4) of tuple type

# attrgetter() similar to itemgetter() but takes attribute(s) names unlike indexes in itemgetter()
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print("Running test method.....")

    def myMethod(self, e, f, *, g):
        print(e, f, g)

obj = MyClass()
prop_a = operator.attrgetter('a')
print(type(prop_a))     # <class 'operator.attrgetter'> which is a callable
print(prop_a(obj))      # 10

# we can call directly as
print(operator.attrgetter('b')(obj))    # 20

# multiple attributes at a time
prop_ab = operator.attrgetter('a', 'b')
print(prop_ab(obj))     # (10, 20)

method_test = operator.attrgetter('test')
print(type(method_test))    # <class 'operator.attrgetter'>
print(type(method_test(obj)))   # <class 'method'>
method_test(obj)()              # Running test method.....

# Applications in sorting
# given list of complex numbers, sort them according to their real part
lst = [2+6j, 1+5j, 8j, 3+2j, -1+6j]
print(sorted(lst, key=operator.attrgetter('real')))     # [(-1+6j), 8j, (1+5j), (2+6j), (3+2j)]

# given a list of tuples, sort them based on their first element
lst = [(3, 2, 1), (1, 4), (6,), (-1, 5), (2, 4, 7, 6)]
print(sorted(lst, key=operator.itemgetter(0)))  # [(-1, 5), (1, 4), (2, 4, 7, 6), (3, 2, 1), (6,)]

# for functions in a class, instead of using attrgetter, we will use methodecaller
# methodcaller will add extra () for calling the method
method_test = operator.methodcaller('test')
method_test(obj)    # Running test method.....
# Note: we don't need to do method_test(obj)() above

# handling methods with arguments
# Using attrgetter()
method_myMethod = operator.attrgetter('myMethod')
method_myMethod(obj)(40, 50, g=60)      # 40 50 60

# using methodcaller()
method_myMethod = operator.methodcaller('myMethod', 40, 50, g=60)
method_myMethod(obj)        # 40 50 60










