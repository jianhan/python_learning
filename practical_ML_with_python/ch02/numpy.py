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
