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

# For prediction of the response variable here, we will learn a Lasso model. A Lasso model is an extension
# of the normal linear regression model which allows us to apply L1 regularization to the model. Simply put, a
# lasso regression will try to minimize the number of independent variables in the final model. This will give
# us the model with the most important variables only (feature selection)

from sklearn.linear_model import Lasso
import numpy as np
from sklearn import datasets
from sklearn.model_selection import GridSearchCV

diabetes = datasets.load_diabetes()
X_train = diabetes.data[:310]
y_train = diabetes.target[:310]
X_test = diabetes.data[310:]
y_test = diabetes.data[310:]
lasso = Lasso(random_state=0)
alphas = np.logspace(-4, -0.5, 30)
estimator = GridSearchCV(lasso, dict(alpha=alphas))
print(estimator.fit(X_train, y_train))
