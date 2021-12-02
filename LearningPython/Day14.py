# global and non-local scopes
a1 = 100
def fun1():
    global a1
    a1 = 'python'
    print(a1)
# fun1()      # python
# print(a1)   # python

def fun2():
    a1 = 'ayush'
    print(a1)
# fun2()      # ayush
# print(a1)   # 100

def fun3():
    a1='ayush'

    def inner():
        nonlocal a1
        a1 = 'python'

    print('before inner a1 :', a1)
    inner()
    print('after inner a1:', a1)

# fun3()  # before inner a1 : ayush\nafter inner a1: python

def fun4():
    a1 = 'ayush'

    def inner1():
        def inner2():
            nonlocal a1
            a1 = 'python'
        inner2()
    print('Before inner1() a1:', a1)
    inner1()
    print('After inner1() a1:', a1)

# fun4()      # Before inner1() a1: ayush\nAfter inner1() a1: python

def fun5():
    a1 = 'ayush'

    def inner1():
        nonlocal a1
        a1 = 'python'

        def inner2():
            nonlocal a1
            a1 = 'awesome'
        print('Before inner2() a1:', a1)    # ayush
        inner2()
        print('After inner() a1: ', a1)     # python
    print('Before inner1() a1:', a1)        # awesome
    inner1()
    print('After inner1() a1', a1)          # awesome

# fun5()

# def fun6():
#     global a1
#     a1 = 'ayush'
#
#     def inner1():
#         nonlocal a1
#         a1 = 'python'
#     inner1()

# fun6()      # Error, SyntaxError: no binding for nonlocal 'a1' found
# NOTE: nonlocal doesn't look for variable bindings in global scopes,
# it only looks for the binding in enclosing local scopes
