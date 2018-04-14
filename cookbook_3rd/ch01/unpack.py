"""
Problem
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variable

Tips:
Unpacking actually works with any object that happens to be iterable, not just tuples or
lists. This includes strings, files, iterators, and generators. For examp
"""

# simple example
p = (4, 5)
x, y = p
print(x)
print(y)
# array

# list example
data = ["Jim Smith", 24, (1, 2, 3)]
name, age, price = data
print(name)
print(age)
print(price)

"""
Problem
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return middle


grades = [1, 2, 3, 4, 5, 6]
print(drop_first_last(grades))
