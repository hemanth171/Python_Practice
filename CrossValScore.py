from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=5)
clf = DecisionTreeClassifier(max_depth=5)
scores_knn = cross_val_score(knn, X, y, scoring='accuracy', cv=10)
scores_clf = cross_val_score(clf, X, y, scoring='accuracy', cv=10)

print scores_knn
print scores_clf
