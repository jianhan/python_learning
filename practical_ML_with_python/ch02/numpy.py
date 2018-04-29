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

# pandas
import pandas as pd

d = [{'city': 'Delhi', "data": 1000},
     {'city': 'Bangalore', "data": 2000},
     {'city': 'Mumbai', "data": 1000}]
df = pd.DataFrame(d).head(2)
print(df.tail())

# read CSV
city_data = pd.read_csv(filepath_or_buffer='simplemaps-worldcities-basic.csv')
city_data.head(n=10)
print(city_data, city_data.tail())
series_es = city_data.lat
print(type(series_es), series_es, series_es[1:10:2], len(series_es))

# pick row and column
print(city_data.iloc[:5, :4])

# want to select cities that have population of more than 10
# million and select columns that start with the letter l:
print("***",
      city_data[city_data['pop'] > 10000000][city_data.columns[pd.Series(city_data.columns).str.startswith('l')]])

# Value attribute
df = pd.DataFrame(np.random.randn(8, 3), columns=['A', 'B', 'C'])
print(df, df.values)

# Descriptive Statistics Functions
# A general practice of dealing with datasets is to know as much about them as possible. Descriptive statistics
# of a dataframe give data scientists a comprehensive look into important information about any attributes
# and features in the dataset.
columns_numeric = ['lat', 'lng', 'pop']
print(city_data[columns_numeric].mean(), city_data[columns_numeric].sum(), city_data[columns_numeric].count(),
      city_data[columns_numeric].median(), city_data[columns_numeric].quantile(0.8))

# All these operations were applied to each of the columns, the default behavior. We can also get all these
# statistics for each row by using a different axis. This will give us the calculated statistics for each row in the dataframe.
print("**", city_data[columns_numeric].sum(axis=1))

# Pandas also provides us with another very handy function called describe. This function will calculate
# the most important statistics for numerical data in one go so that we don’t have to use individual functions.
print(city_data[columns_numeric].describe())
