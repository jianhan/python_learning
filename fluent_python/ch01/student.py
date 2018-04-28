import pandas as pd

# step 1 data prepration
pd.options.mode.chained_assignment = None  # default='warn'
df = pd.read_csv("./student_records.csv")

# step 2 feature extraction
feature_names = ['OverallGrade', 'Obedient', 'ResearchScore', 'ProjectScore']
training_features = df[feature_names]
outcome_name = ["Recommend"]
outcome_labels = df[outcome_name]

# list down features based on type
# separate out our available features based on their type
numeric_feature_names = ['ResearchScore', 'ProjectScore']
categoricial_feature_names = ['OverallGrade', 'Obedient']

# We will now use a standard scalar from scikit-learn to scale or normalize our two numeric scorebased attributes using the following code
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
# fit scaler on numeric features
ss.fit(training_features[numeric_feature_names])
# scale numeric features now
training_features[numeric_feature_names] = ss.transform(training_features[numeric_feature_names])

# Now that we have successfully scaled our numeric features (see Figure 1-29), let’s handle our categorical
# features and carry out the necessary feature engineering needed based on the following code
training_features = pd.get_dummies(training_features, columns=categoricial_feature_names)

categorical_engineered_features = list(set(training_features.columns) - set(numeric_feature_names))

# The following code depicts how to build the supervised model
from sklearn.linear_model import LogisticRegression
import numpy as np

# fit the model
lr = LogisticRegression()
model = lr.fit(training_features, np.array(outcome_labels['Recommend']))
# view model parameters

pred_labels = model.predict(training_features)
actual_labels = np.array(outcome_labels['Recommend'])
# evaluate model performance
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

print('Accuracy:', float(accuracy_score(actual_labels,
                                        pred_labels)) * 100, '%')
print('Classification Stats:')
print(classification_report(actual_labels, pred_labels))

# We built our first supervised learning model, and to deploy this model typically in a system or server, we
# need to persist the model. We also need to save the scalar object we used to scale the numerical features
# since we use it to transform the numeric features of new data samples. The following snippet depicts a way
# to store the model and scalar objects.

from sklearn.externals import joblib
import os

# save models to be deployed on your server
if not os.path.exists('Model'):
    os.mkdir('Model')
if not os.path.exists('Scaler'):
    os.mkdir('Scaler')
joblib.dump(model, r'Model/model.pickle')
joblib.dump(ss, r'Scaler/scaler.pickle')

# Prediction in Action
# We are now ready to start predicting with our newly built and deployed model! To start predictions, we need
# to load our model and scalar objects into memory. The following code helps us do this.

# load model and scaler objects
model = joblib.load(r'Model/model.pickle')
scaler = joblib.load(r'Scaler/scaler.pickle')

## data retrieval
# We have some sample new student records (for two students) for which we want our model to predict if
# they will get the grant recommendation. Let’s retrieve and view this data using the following code.
new_data = pd.DataFrame(
    [{'Name': 'Nathan', 'OverallGrade': 'F', 'Obedient': 'N', 'ResearchScore': 30, 'ProjectScore': 20},
     {'Name': 'Thomas', 'OverallGrade': 'A',
      'Obedient': 'Y', 'ResearchScore': 78, 'ProjectScore': 80}])
new_data = new_data[['Name', 'OverallGrade', 'Obedient',
                     'ResearchScore', 'ProjectScore']]
print(new_data)

## data preparation
prediction_features = new_data[feature_names]
# scaling
prediction_features[numeric_feature_names] = scaler.transform(prediction_features[numeric_feature_names])
# engineering categorical variables
prediction_features = pd.get_dummies(prediction_features, columns=categoricial_feature_names)
# view feature set
print(prediction_features)

# add missing categorical feature columns
current_categorical_engineered_features = set(prediction_features.columns) - set(numeric_feature_names)
missing_features = set(categorical_engineered_features) - current_categorical_engineered_features
for feature in missing_features:
    # add zeros since feature is absent in these data samples
    prediction_features[feature] = [0] * len(prediction_features)
# view final feature set
print(prediction_features)

## predict using model
predictions = model.predict(prediction_features)
## display results
new_data['Recommend'] = predictions
print(new_data)
