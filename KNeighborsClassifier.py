from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

k_range = range(1,11)
accuracy_score_list = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy_score_list.append(metrics.accuracy_score(y_test, y_pred))

print accuracy_score_list

plt.plot(k_range, accuracy_score_list)
plt.ylim(-0.1, 1.1)
plt.xlabel('neighbors_range')
plt.ylabel('accuracy_score')
plt.show()