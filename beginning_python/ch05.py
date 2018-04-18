# Sequence Unpacking
x, y, z = 1, 2, 3
print(x, y, z)

# switch variable

x, y = y, x
print(x, y)

# You can then use the popitem method, which does just that, returning the pair as a tuple. Then you can unpack the
# returned tuple directly into two variables

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key, value)
