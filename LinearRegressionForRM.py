from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/hemanth/Documents/Python_workspace/Udacity_machine-learning_projects/machine-learning/projects/boston_housing/housing.csv')

rooms = data['RM'].reshape(-1,1)
prices = data.MEDV

reg = LinearRegression()
reg.fit(rooms, prices)
y_pred = reg.predict(rooms)

plt.plot(rooms, y_pred, color='red', linewidth=1)
plt.scatter(rooms, prices, c=prices, alpha=0.5)
plt.xlabel('ROOMS')
plt.ylabel('PRICES')
plt.show()