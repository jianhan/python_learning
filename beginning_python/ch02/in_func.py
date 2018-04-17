database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
if ["jones", '9843'] in database: print('Access granted')

l = list("hello world")
print(l, ''.join(l))

# assign slices
name = list('Perl')
name[2:] = list('ar')
print(name, ''.join(name))

# replace with different length
name = list('Perl')
name[1:] = list('ython')
print(name)

# insert without replacing any of the original
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
numbers[2:1] = ["test", "test1"]
print(numbers)

# reverse for deletion
numbers[1:6] = []
print(numbers)
