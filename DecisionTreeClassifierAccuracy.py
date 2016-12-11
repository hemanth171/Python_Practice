from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from sklearn.datasets import load_iris

iris = load_iris()
iris_features = iris.data
iris_target = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_features, iris_target, test_size=0.2, random_state=0)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print 'Accuracy ',accuracy_score(y_test, y_pred)