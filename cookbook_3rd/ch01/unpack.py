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

# case 2
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)

# It is worth noting that the star syntax can be especially useful when iterating over a
# sequence of tuples of varying length. For example, perhaps a sequence of tagged tuples:
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

"""
Star unpacking can also be useful when combined with certain kinds of string processing
operations, such as splitting. For example:
"""

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)
