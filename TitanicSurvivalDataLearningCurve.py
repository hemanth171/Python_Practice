import pandas as pd
import numpy as np
import sklearn.learning_curve as curves
import matplotlib.pyplot as plt

from sklearn.cross_validation import ShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/titanic_survival_exploration/titanic_data.csv')
data = data._get_numeric_data()
target = data['Survived']
features = data.drop(['Age', 'Survived'], axis=1)

train_sizes = np.rint(np.linspace(1, features.shape[0]*0.8-1, 9)).astype(int)
cv = ShuffleSplit(features.shape[0], n_iter=10, test_size=0.2, random_state=0)

plt.figure(1, figsize=(15, 10))
for k, min_sample in enumerate([30,40,50,60]):
    estimator = DecisionTreeClassifier(min_samples_split=min_sample)
    
    sizes, train_scores, test_scores = curves.learning_curve(estimator, features, target, train_sizes=train_sizes, cv=cv, scoring='accuracy')
    
    train_std = np.std(train_scores, axis=1)
    train_mean = np.mean(train_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    
    plt.subplot(2, 2, k+1)
    plt.plot(sizes, train_mean, 'o-', color='r', label='Training score')
    plt.plot(sizes, test_mean, 'o-', color='g', label='Testing score')
    plt.fill_between(sizes, train_mean-train_std, train_mean+train_std, alpha=0.15, color='r')
    plt.fill_between(sizes, test_mean-test_std, test_mean+test_std, alpha=0.15, color='g')
    plt.xlabel('Number of training points')
    plt.ylabel('Score')
    plt.xlim(0, features.shape[0]*0.8-1)
    plt.ylim(-0.05, 1.05)
    plt.title('min_split=%s'%(min_sample))
    
plt.legend(loc = 'lower right')
plt.tight_layout()
plt.show()