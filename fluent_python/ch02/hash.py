# All mapping types in the standard library use the basic dict in their implementation,
# so they share the limitation that the keys must be hashable

# An object is hashable if it has a hash value which never changes during its lifetime

# The atomic immutable types (str, bytes, numeric types) are all hashable. A frozen
# set is always hashable, because its elements must be hashable by definition. A tuple is
# hashable only if all its items are hashable. See tuples tt, tl and tf:

tt = (1, 2, (30, 40))
print(hash(tt))
