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
