# a string is just a sequence of characters. the index 0 refers to the first element, in this case the
# letter H. unlike some other languages, there is no separate character type, though. a character is just a singleelement string
greeting = 'Hello'
print(greeting[0])

# -1 is from last element
print(greeting[-1])

# String literals
print('Hello'[1])

# If a function call returns a sequence, you can index it directly
# fourth = input('Year: ')[3]
# print(fourth)

# index
# The first index is the number of the first element you want to include. However, the last index is the number
# of the first element after your slice.
# where the first is inclusive and the second is exclusive.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])

# negative
print(numbers[-3:-1])
print(numbers[-3:])

# step
print(numbers[0:10:2])
print(numbers[::4])

# for a positive step size, it moves from the
# beginning toward the end, and for a negative step size, it moves from the end toward the beginning.
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[0:10:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])

# concat
print([1, 2, 3] + [4, 5, 6])

# multiplication
print([1, 2, 3] * 5)
