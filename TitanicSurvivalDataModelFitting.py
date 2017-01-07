import pandas as pd
import numpy as np

from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import ShuffleSplit
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/titanic_survival_exploration/titanic_data.csv')
data = data._get_numeric_data()
target = data['Survived']
features = data.drop(['Age', 'Survived'], axis=1)

def fit_model(X, y):
    cv = ShuffleSplit(X.shape[0], n_iter=10, test_size=0.2, random_state=0)
    
    estimator = DecisionTreeClassifier()
    
    param_grid = {'min_samples_split': list(np.linspace(30, 150, 12).astype(int))}
    
    grid = GridSearchCV(estimator, param_grid, scoring='accuracy', cv=cv)
    
    grid = grid.fit(X, y)
    
    return grid.best_estimator_

print fit_model(features, target)