from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')

lstat = data['LSTAT'].reshape(-1,1)
prices = data.MEDV

reg = LinearRegression()
dec_reg = DecisionTreeRegressor(max_depth=1)
dec_reg.fit(lstat, prices)
y = dec_reg.predict(lstat)
reg.fit(lstat, prices)
y_pred = reg.predict(lstat)

plt.plot(lstat, y, color='red', linewidth=1)
plt.scatter(lstat, prices, c=prices, alpha=0.5)
plt.xlabel('LSTAT')
plt.ylabel('PRICE')
plt.show()