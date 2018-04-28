import pandas as pd

# step 1 data prepration
pd.options.mode.chained_assignment = None  # default='warn'
df = pd.read_csv("./student_records.csv")
print(df)

# step 2 feature extraction
feature_names = ['OverallGrade', 'Obedient', 'ResearchScore', 'ProjectScore']
training_features = df[feature_names]
outcome_name = ["Recommend"]
outcome_labels = df[outcome_name]
print(outcome_labels)

# list down features based on type
# separate out our available features based on their type
numeric_feature_names = ['ResearchScore', 'ProjectScore']
categoricial_feature_names = ['OverallGrade', 'Obedient']

# We will now use a standard scalar from scikit-learn to scale or normalize our two numeric scorebased attributes using the following code
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
# fit scaler on numeric features
ss.fit(training_features[numeric_feature_names])
print(training_features[numeric_feature_names])
# scale numeric features now
training_features[numeric_feature_names] = ss.transform(training_features[numeric_feature_names])

# Now that we have successfully scaled our numeric features (see Figure 1-29), let’s handle our categorical
# features and carry out the necessary feature engineering needed based on the following code
training_features = pd.get_dummies(training_features, columns=categoricial_feature_names)
print(training_features)

categorical_engineered_features = list(set(training_features.columns) - set(numeric_feature_names))
print(categorical_engineered_features)

# The following code depicts how to build the supervised model
from sklearn.linear_model import LogisticRegression
import numpy as np

# fit the model
lr = LogisticRegression()
model = lr.fit(training_features, np.array(outcome_labels['Recommend']))
# view model parameters
print(model)

pred_labels = model.predict(training_features)
actual_labels = np.array(outcome_labels['Recommend'])
# evaluate model performance
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

print('Accuracy:', float(accuracy_score(actual_labels,
                                        pred_labels)) * 100, '%')
print('Classification Stats:')
print(classification_report(actual_labels, pred_labels))
