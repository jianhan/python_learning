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
