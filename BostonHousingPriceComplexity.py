import pandas as pd
import numpy as np
import sklearn.learning_curve as curves
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import ShuffleSplit

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

cv = ShuffleSplit(features.shape[0], n_iter=10, test_size=0.2, random_state=0)

param_range = np.arange(1,11)

train_scores, test_scores = curves.validation_curve(DecisionTreeRegressor(), features, prices, param_name='max_depth', param_range=param_range, cv=cv, scoring='r2')

train_std = np.std(train_scores, axis=1)
train_mean = np.mean(train_scores, axis=1)
test_std = np.std(test_scores, axis=1)
test_mean = np.mean(test_scores,axis=1)

plt.plot(param_range, train_mean, 'o-', color='r', label='Training score')
plt.plot(param_range, test_mean, 'o-', color='g', label='Validation score')
plt.fill_between(param_range, train_mean-train_std, train_mean+train_std, alpha=0.15,color='r')
plt.fill_between(param_range, test_mean-test_std, test_mean+test_std, alpha=0.15, color='g')
plt.xlabel('Maximum depth')
plt.ylabel('Score')
plt.legend(loc = 'lower right')
plt.title('Decision Tree Regressor Complexity Performance')
plt.ylim(-0.05,1.05)
plt.show()