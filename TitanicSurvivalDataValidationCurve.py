import pandas as pd
import numpy as np
import sklearn.learning_curve as curves
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import ShuffleSplit

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/titanic_survival_exploration/titanic_data.csv')
data = data._get_numeric_data()
target = data['Survived']
features = data.drop(['Age', 'Survived'], axis=1)

param_range = list(np.linspace(30, 150, 12).astype(int))

cv = ShuffleSplit(features.shape[0], n_iter=10, test_size=0.2, random_state=0)

train_scores, test_scores = curves.validation_curve(DecisionTreeClassifier(), features, target, param_name='min_samples_split', param_range=param_range, cv=cv, scoring='accuracy')

train_std = np.std(train_scores, axis=1)
train_mean = np.mean(train_scores, axis=1)
test_std = np.std(test_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)

plt.plot(param_range, train_mean, 'o-', color='r', label='Training Score')
plt.plot(param_range, test_mean, 'o-', color='g', label='Validation Score')
plt.fill_between(param_range, train_mean-train_std, train_mean+train_std, alpha=0.15, color='r')
plt.fill_between(param_range, test_mean-test_std, test_mean+test_std, alpha=0.15, color='g')
plt.legend(loc = 'lower right')
plt.ylim(-0.05, 1.05)
plt.xlabel('min_samples_split')
plt.ylabel('Score')
plt.show()