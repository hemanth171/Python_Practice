from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')

pt_ratio = data['PTRATIO'].reshape(-1,1)
prices = data.MEDV

reg = LinearRegression()

reg.fit(pt_ratio, prices)

y_predict = reg.predict(pt_ratio)

plt.plot(pt_ratio, y_predict, color='red', linewidth=1)
plt.scatter(pt_ratio, prices, alpha=0.5, c=prices)
plt.xlabel('PTRATIO')
plt.ylabel('PRICE')
plt.show()