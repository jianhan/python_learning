test_str = "this is a test string"
print(tuple(ord(s) for s in test_str))

# generate array
import array

print(array.array('I', (ord(s) for s in test_str)))
