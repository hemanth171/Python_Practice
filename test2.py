import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.learning_curve as curves
from sklearn.cross_validation import ShuffleSplit
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)
# a = [3,6,9,1,4,8]
# print np.sort(a)
# print np.median(a)

# y_true = [3, -0.5, 2, 7]
# y_pred = [5, 1, 4, 9]
# output = r2_score(y_true, y_pred)
# print output

#print features.shape[0]
cv = ShuffleSplit(features.shape[0], n_iter=10, test_size=0.2, random_state=0)
train_sizes = np.rint(np.linspace(1, features.shape[0]*0.8 - 1, 9)).astype(int)
regressor = DecisionTreeRegressor(max_depth=9)

sizes, train_scores, test_scores = curves.learning_curve(regressor, features, prices, train_sizes=train_sizes, cv=cv, scoring='r2')

train_std = np.std(train_scores, axis = 1)
train_mean = np.mean(train_scores, axis = 1)
test_std = np.std(test_scores, axis = 1)
test_mean = np.mean(test_scores, axis = 1)

plt.plot(sizes, train_mean, 'o-', color='r', label='Training score')
plt.plot(sizes, test_mean, 'o-', color='g', label='Testing score')
plt.fill_between(sizes, train_mean - train_std, train_mean + train_std, alpha = 0.15, color = 'r')
plt.fill_between(sizes, test_mean - test_std, test_mean + test_std, alpha = 0.15, color = 'g')
plt.legend(bbox_to_anchor=(1.1, 1.1))
plt.show()
#def ModelLearning(X, y):
    