# function annotations and docstrings
# annotations are like the meta data attached and docstrings are the document strings
def fact(n: 'int >= 0') -> 'factorial of n':
    """helps to calculate factorial of a given number
    input : n (a non-negative integer)
    output: factorial of n"""
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


print(fact(5))
help(fact)
print("Doc string of fact() : \n", fact.__doc__)  # stores the document string
print("annotations of fact() : \n", fact.__annotations__)  # stores the annotations in form of dictionary
