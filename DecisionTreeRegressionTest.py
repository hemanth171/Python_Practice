from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd

X = [[0,0],[1,1],[2,2]]
y = [0,1,2]
clf = DecisionTreeRegressor()
clf = clf.fit(X, y)
#print clf.predict([1,2])

#print np.arange(0.,5.0,0.01)[:, np.newaxis]

a = pd.DataFrame(X)