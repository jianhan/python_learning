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

# zip

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
    break
else:
    print("Didn't find it!")

# comperhension
print([x * x for x in range(10)])

# division
print(x * x for x in range(10) if x % 3 == 0)

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

# a better solution

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])

# delete
x = ["Hello", "world"]
y = x
y[1] = "Python"
print(x)
del x
print(y)

# reference number
x = 1
y = x
y = 2
print(x)

# reference list. Notice this case, the change of Y will result the change of X because y changes the value of list
x = [1, 2, 3]
y = x
y[0] = 100
print(x)

# is operator and ==
names = ["James", "Jack"]
n = names
print(n is names, n == names, n)

# now change n
n[0] = "Ray"
print(n is names, n == names, n)

x = names[:]
print(x is names, x == names, x)


def hello(name="Hello", value="world"):
    print('{}, {} !'.format(name, value))


hello("Hello", "World")


# optional
def hello_4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))


hello_4('Mars')
hello_4('Mars', 'Howdy')
hello_4('Mars', 'Howdy', '...')
hello_4('Mars', punctuation='.')
hello_4('Mars', greeting='Top of the morning to ya')


# collection params

def print_params(*params):
    print(params)


print_params('Testing')

print_params(1, 2, 3)


# names
def my_hello(hello, world):
    print(hello, world)


my_hello(world="HHH", hello="WWWW")


# collection in the middle, must called by name
def in_the_middle(x, *y, z):
    print(x, y, z)


in_the_middle("Test", 1, 2, 3, 4, 5, z="testz")


# double start returns a dictionary
def return_dictionary(**params):
    print(params)


# must pass key value like following
return_dictionary(x=1, y=2, z=3)


# mix and match
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)


def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))


params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)
