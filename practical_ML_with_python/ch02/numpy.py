import numpy as np

arr = np.array([1, 3, 5, 6, 7, 8, 9])
arr2 = np.array(["test1", "test2"])
print(arr, arr.shape, arr.dtype, arr2.dtype)

# Often, an important requirement is to initialize an array of a specified dimension with random values.
# This can be done easily by using the randn function from the numpy.random package

arr = np.random.randn(3, 4)
print(arr)

# advance index
arr = np.arange(9).reshape(3, 3)
# In this example we have provided an array in which the first part identifies the rows we want to access
# and the second identifies the columns which we want to address. This is quite similar to providing a

# collective element-wise address.
print(arr[[0, 1, 2], [1, 0, 0]])

# boolean index
cities = np.array(["delhi", "bangalore", "mumbai", "chennai", "bhopal"])
city_data = np.random.randn(5, 3)
print(city_data[cities == "delhi"], "***", city_data[city_data > 0])

# sub example
city_data[city_data > 0] = 0
print(city_data)

# modf
# The function modf will return the fractional and the integer part of the input supplied to it
arr1 = np.random.randn(5, 3)
print(np.modf(arr1))

# Linear Algebra Using numpy
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [1, 2, 3]])
print(A.dot(B))

# T operator

A = np.arange(15).reshape(3, 5)
print("***", A, A.T)

#  decomposition of a matrix
print(np.linalg.svd(A))

# Linear algebra is often also used to solve a system of equations.
# x + 5y -3z = 16
# 3x - 5y + 2z = -8
# 5x + 3y - 7z = 0

a = np.array([[7, 5, -3], [3, -5, 2], [5, 3, -7]])
b = np.array([16, -8, 0])
x = np.linalg.solve(a, b)
print(x)

# We can also check if the solution is correct using the np.allclose function.
print(np.allclose(np.dot(a, x), b))
