# Applications of closures
from time import perf_counter, sleep

# First Application: Averager
# Using class
class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

f1 = Averager()
print(f1.add(10))   # 10
print(f1.add(20))   # 15
print(f1.add(30))   # 20

# Using closure
def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count
    return add

f2 = averager()
print(f2(10))   # 10
print(f2(20))   # 15
print(f2(30))   # 20

# Second application(using class): object life timer
class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
print(t1())     # 5.13200000000491e-06
sleep(5)
print(t1())     # 4.9998516429999995

# Object timer function using closures
def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start
    return poll
t2 = timer()
print(t2())     # 1.8659999998504873e-06
sleep(5)
print(t2())     # 5.002333126000001