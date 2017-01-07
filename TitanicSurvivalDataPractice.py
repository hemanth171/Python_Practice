import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score, ShuffleSplit

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/titanic_survival_exploration/titanic_data.csv')
data = data._get_numeric_data()
target = data['Survived']
features = data.drop(['Age', 'Survived'], axis=1)

#X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)
cv = ShuffleSplit(features.shape[0], n_iter=9, test_size=0.2, random_state=0)

# train_sizes = np.rint(np.linspace(1, features.shape[0]*0.8, 9)).astype(int)
# print train_sizes

k_range = np.arange(1,10)
plt.figure(1, figsize=(16, 10))
 
for k in k_range:
    estimator = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(estimator, features, target, scoring='accuracy', cv=cv)
  
    plt.subplot(3, 3, k) 
    plt.plot(k_range, score, 'o-', color='r', label='accuracy score')
    plt.xlabel('Maximum neighbors')
    plt.ylabel('Score')
    plt.ylim(-0.05, 1.05)
    plt.title('max neighbors=%s'%(k))
     
plt.legend(loc = 'lower right')
plt.tight_layout()
plt.show()