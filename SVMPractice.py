from sklearn.datasets import load_iris
from sklearn.svm import SVC
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data[:, :2]
y = iris.target

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.5)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()