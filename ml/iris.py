import pandas as pd

print("pandas version: %s" % pd.__version__)
import matplotlib

print("matplotlib version: %s" % matplotlib.__version__)
import numpy as np

print("numpy version: %s" % np.__version__)

import IPython

print("IPython version: %s" % IPython.__version__)
import sklearn

print("scikit-learn version: %s" % sklearn.__version__)

from sklearn.datasets import load_iris

iris = load_iris()
print(iris['data'].shape)
# print(len(iris['data']))
# print(iris.keys())
# print(iris['DESCR'][:2000])
