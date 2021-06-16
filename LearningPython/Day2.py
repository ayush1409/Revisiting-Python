# Packing and Unpacking of iterables

l = [1, 2, 3, 4, 5, 6]
# using list splicing (work only with indexable iterables i.e does not work with sets and dictonaries)
a, b = l[0], l[1:]
print(a, b)

# using * operator
a, *b = l
print(a, b)
a, *b, c = l
print(a, b, c)
a, b, *c, d = l
print(a, b, c, d)
# NOTE: b is unpacked to a list(which is mutable), irrespective of the type of l

# nested unpacking
l = [1, 2, 3, 4, 'xyz']
a, *b, (c, *d) = l
print(a, b, c, d)

# joining two iterables
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]      # Joining two lists
print(l)
s = 'abc'
l = [*l1, *s]       # Joining a list and a string
print(l)
x = {*l1, *s}       # Unpacking to a set
print(x)

# union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
s = s1.union(s2).union(s3).union(s4)
print(s)
s = s1.union(s2, s3, s4)
print(s)
s = {*s1, *s2, *s3, *s4}
print(s)
l = [*s1, *s2, *s3, *s4]    # when we need to preserve the repeated elements
print(l)


# Unpacking with dictionaries
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
e = {'d': 5, 'e': 6}
# unpacking of keys
f = *d, *e
print(f)
# unpacking of key-value pairs
g = {**d, **e}
print(g)
