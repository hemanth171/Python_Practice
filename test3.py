import pandas as pd
import numpy as np
import sklearn.learning_curve as curves
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import ShuffleSplit

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

train_sizes = np.rint(np.linspace(1, features.shape[0]*0.8-1, 9)).astype(int)

cv = ShuffleSplit(features.shape[0], n_iter=10, test_size=0.2, random_state=0)

plt.figure(1, figsize=(15,10))

for k, depth in enumerate([1,2,3,4,5,6,7,8,9]):
    estimator = DecisionTreeRegressor(max_depth=depth)
    
    sizes, train_scores, test_scores = curves.learning_curve(estimator, features, prices, train_sizes=train_sizes, cv=cv, scoring='r2')
    
    train_std = np.std(train_scores, axis=1)
    train_mean = np.mean(train_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    
    plt.subplot(3, 3, k+1)
    plt.plot(sizes, train_mean, 'o-', color='r', label='training score')
    plt.plot(sizes, test_mean, 'o-', color='g', label='testing score')
    plt.fill_between(sizes, train_mean-train_std, train_mean+train_std, alpha=0.15, color='r')
    plt.fill_between(sizes, test_mean-test_std, test_mean+test_std, alpha=0.15, color='g')
    plt.title('max_depth=%s'%(depth))
    plt.xlim(0, features.shape[0]*0.8-1)
    plt.ylim(-0.05, 1.05)
    plt.xlabel('Number of Training Points')
    plt.ylabel('Score')

plt.legend(loc = 'lower right')
plt.tight_layout()
plt.show()
