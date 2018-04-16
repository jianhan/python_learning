# concat string
print("I am " 'json')

# concat with variable

first = "James"
last = "bond"

# The following will not work
# print(first last)
print(first + last)

"""
With str, you convert a value into a string in some reasonable
fashion that will probably be understood by a user, 
"""
print(str("Hello,\nworld!"))

"""
If you use repr, however, you will generally get a
representation of the value as a legal Python expression.
"""
print(repr("Hello,\nworld!"))

# Long string example, You can also use triple double quotes, """like this""". Note that because of the distinctive enclosing
# quotes, both single and double quotes are allowed inside, without being backslash-escaped
print('''Underneath the downhill breezes a mistake. 
The cloth graces the historical bastard past a warehouse. 
Will the questionable device swing? Why can't the taxpayer cruise? Each romantic sin persists within the stare. 
A century pumps beneath an example!''')

print("""Underneath the downhill breezes a mistake. 
The cloth graces the historical bastard past a warehouse. 
Will the questionable device swing? Why can't the taxpayer cruise? Each romantic sin persists within the stare. 
A century pumps beneath an example!""")

# Ordinary strings can also span several lines. If the last character on a line is a backslash, the line
# break itself is “escaped” and ignored. For example:
print \
    ('Hello, world', "My name is James")

# Raw string
# Raw strings are useful in such cases. They don’t treat the backslash as a special character at all. Every
# character you put into a raw string stays the way you wrote it.
path = 'C:\\Program Files\\fnord\\foo\\bar\\baz\\frozz\\bozz'
print(path)
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')

# As you can see, raw strings are prefixed with an r. It would seem that you can put anything inside a raw
# string, and that is almost true. Quotes must be escaped as usual, although that means you get a backslash in
# your final string, too.
print(r'Let\'s go!')

# The one thing you can’t have in a raw string is a lone, final backslash. In other words, the last character in
# a raw string cannot be a backslash unless you escape it

# Not allowed
# print(r"This is illegal\")

# Okay, so it’s reasonable, but what if you want the last character in your raw string to be a backslash? (Perhaps
# it’s the end of a DOS path, for example.) Well, I’ve given you a whole bag of tricks in this section that should
# help you solve that problem, but basically you need to put the backslash in a separate string. A simple way of
# doing that is the following:
print(r'C:\Program Files\foo\bar' '\\')
