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

# Long string example
print('''Underneath the downhill breezes a mistake. 
The cloth graces the historical bastard past a warehouse. 
Will the questionable device swing? Why can't the taxpayer cruise? Each romantic sin persists within the stare. 
A century pumps beneath an example!''')

print("""Underneath the downhill breezes a mistake. 
The cloth graces the historical bastard past a warehouse. 
Will the questionable device swing? Why can't the taxpayer cruise? Each romantic sin persists within the stare. 
A century pumps beneath an example!""")
