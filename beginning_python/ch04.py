# dict You can use the dict function1 to construct dictionaries from other mappings (for example, other
# dictionaries) or from sequences of (key, value) pairs.

items = [('name', 'Gumby'), ('age', 42), ('phone', 123123123)]
d = dict(items)
print(d)

# It can also be used with keyword arguments, as follows:
d = dict(name='Gumby', age=42)
print(d)

# string formatting
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}

print("Cecil's phone number is {Cecil}.".format_map(phonebook))

# template parse
template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))
