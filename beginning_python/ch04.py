# dict You can use the dict function1 to construct dictionaries from other mappings (for example, other
# dictionaries) or from sequences of (key, value) pairs.

items = [('name', 'Gumby'), ('age', 42), ('phone', 123123123)]
d = dict(items)
print(d)

# It can also be used with keyword arguments, as follows:
d = dict(name='Gumby', age=42)
print(d)
