# 1. What is the baseline prediction of disease progression for future patients?

# 2. Which independent variables (features) are important factors for predicting disease
# progression?
from sklearn import datasets

diabetes = datasets.load_diabetes()
y = diabetes.target
X = diabetes.data
print(y, X, X.shape)

# Since we are using the data in the form of numpy arrays, we don’t get the name of the features in the data
# itself. But we will keep the reference to the variable names as they may be needed later in our process or just
# for future reference.
feature_names = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
