import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import ShuffleSplit

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')

feature_cols = ['RM', 'LSTAT', 'PTRATIO']
X = data[feature_cols]
y = data.MEDV

regressor = DecisionTreeRegressor(max_depth=5)
scores = cross_val_score(regressor, X, y, scoring='mean_squared_error', cv=10)

cv = ShuffleSplit(X.shape[0], n_iter=10, test_size=0.2, random_state=0)
train_sizes = np.rint(np.linspace(1, X.shape[0]*0.8 - 1, 9)).astype(int)
print np.linspace(1, X.shape[0]*0.8 - 1, 9)
print X.shape[0]*0.8-1

mse_scores = -scores
rmse_scores = np.sqrt(mse_scores)
