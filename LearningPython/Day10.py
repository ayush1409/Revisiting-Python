# filter, map and zip

# MAP
# map(fun, *iterables)  applies fun to each element of corresponding element of iterables
# fun is applied till the shortest iterable range
lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, lst)))     # OUTPUT: [1, 4, 9, 16, 25]

# alternative list comprehension
print([x ** 2 for x in lst])    # OUTPUT: [1, 4, 9, 16, 25]

lst1 = [6, 7, 8, 9]
print(list(map(lambda x, y: x + y, lst, lst1)))     # OUTPUT: [7, 9, 11, 13]

# alternative list comprehension
print([x + y for x, y in zip(lst, lst1)])      # OUTPUT: [7, 9, 11, 13]

# FILTER: filter() is used to filter based on result return by a function(truthy then keep, else discard)
# filter(fun, iterable): takes a function and one iterable
print(list(filter(lambda x: x % 2 == 0, lst)))      # OUTPUT: [2, 4]
print(list(filter(None, lst)))      # OUTPUT: [1, 2, 3, 4, 5]
# Note: if fun is None, then the result will be the input (no changes done)

# alternative list comprehension
print([x for x in lst if x % 2 == 0])   # OUTPUT: [2, 4], very expressive

# ZIP: zip(*iterables) takes multiple iterators and zip their corresponding elements
lang = 'python'
print(list(zip(lst, lst1, lang)))   # OUTPUT: [(1, 6, 'p'), (2, 7, 'y'), (3, 8, 't'), (4, 9, 'h')]

# combining filter and map
print(list(filter(lambda y: y < 25, map(lambda x: x**2, lst))))     # OUTPUT: [1, 4, 9, 16]

# alternative list comprehension
print([x**2 for x in lst if x**2 < 25])     # OUTPUT: [1, 4, 9, 16], very much expressive


