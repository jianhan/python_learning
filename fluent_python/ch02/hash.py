# All mapping types in the standard library use the basic dict in their implementation,
# so they share the limitation that the keys must be hashable

# An object is hashable if it has a hash value which never changes during its lifetime

# The atomic immutable types (str, bytes, numeric types) are all hashable. A frozen
# set is always hashable, because its elements must be hashable by definition. A tuple is
# hashable only if all its items are hashable. See tuples tt, tl and tf:

tt = (1, 2, (30, 40))
print(hash(tt))

tl = (1, 2, [30, 40])
# Following will print error can not be hashed
# print(hash(tl))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# Given these ground rules, you can build dictionaries in several ways. The Built-in
# Types page in the Library Reference has this example to show the various means of
# building a dict:

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
