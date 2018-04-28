import numpy as np

arr = np.array([1, 3, 5, 6, 7, 8, 9])
arr2 = np.array(["test1", "test2"])
print(arr, arr.shape, arr.dtype, arr2.dtype)

# Often, an important requirement is to initialize an array of a specified dimension with random values.
# This can be done easily by using the randn function from the numpy.random package

arr = np.random.randn(3, 4)
print(arr)
