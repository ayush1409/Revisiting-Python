# Working with closures
def fun1():
    x = 'python'
    print(hex(id(x)))  # 0x3215680

    def inner1():
        nonlocal x
        x = 'awesome'
        print(x)
    return inner1

f1 = fun1()
f1()    # awesome
print(f1.__code__.co_freevars)      # ('x', )
print(f1.__closure__)               # (<cell at 0x03081FB8: str object at 0x032156C0>,)

# different outer funtions uses different scope
def counter1():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count
    return inc

# NOTE: each counter (c1, c2) has seperate scopes
c1 = counter1()
c2 = counter1()
# Check for the different scopes (different cell address)
print(c1.__closure__, c2.__closure__)
# (<cell at 0x00F9C1A8: int object at 0x657FA7A0>,) (<cell at 0x00F9C1C0: int object at 0x657FA7A0>,)
print(c1())     # 1
print(c1())     # 2
print(c1())     # 3
print(c2())     # 1

# shared scopes
def counter2():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

c3, c4 = counter2()
# Check for shared scope (same cell address)
print(c3.__closure__, c4.__closure__)
# (<cell at 0x02C1C238: int object at 0x657FA7A0>,) (<cell at 0x02C1C238: int object at 0x657FA7A0>,)
print(c3())     # 1
print(c3())     # 2
print(c4())     # 3

# Nested Closures - concept of decorators
def incrementer(n: "step size"):
    def inner(start: "start value of counter"):
        current = start

        def inc():
            nonlocal current
            current += n
            return current
        return inc
    return inner

fn = incrementer(2)
print(fn.__code__.co_freevars)      # ('n')
inc_2 = fn(100)
print(inc_2.__code__.co_freevars)   # ('current', 'n')

print(inc_2())      # 102
print(inc_2())      # 104

# Concept of lambda functions with shared variable
def adder(n):
    def inner(x):
        x += n
        return x
    return inner

adder1 = adder(1)
adder2 = adder(2)
adder3 = adder(3)

print(adder1(10))   # 11
print(adder2(10))   # 12
print(adder2(10))   # 13

# suppose we want to implement above adders using loop
def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders
# The problem with the above code is n is shared between all the adders
# i.e. adder[0](10), adder[1](10) and adder[2](10) will give same answer i.e. 13
# Note: adders functions are not closures, they are of lambda types

# How to solve above problem
def create_adders_again():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x+y)
    return adders
# Note that, the default value of parameters is evaluated in compile time
adder = create_adders_again()
print(adder[0](10))     # 11
print(adder[1](10))     # 12
print(adder[2](10))     # 13



