import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('/Users/hemanth/Documents/Python_workspace/titanic_survival_exploration/titanic_data.csv')

# Limit to categorical data
X = X.select_dtypes(include=[object])
#print X

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()

for feature in X:
    X[feature] = le.fit_transform(X[feature])
#print X

enc = OneHotEncoder()
enc.fit(X)
#print enc.n_values_

onehotlabels = enc.transform(X)
print onehotlabels