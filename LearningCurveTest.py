import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import ShuffleSplit
from sklearn.learning_curve import learning_curve

def plotting_learning_curve(estimator,X,y,train_sizes=np.linspace(.1,1.0,5),cv):
    plt.xlabel('Training example')
    plt.ylabel('Score')
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, train_sizes, cv)
    

digits = load_digits()
X, y = digits.data, digits.target
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
estimator = GaussianNB()
