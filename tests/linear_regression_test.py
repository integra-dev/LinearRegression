import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

import pandas as pd

data = pd.read_csv('../csv_test/kaggle/linnerud_exercise.csv', delimiter='\s+', index_col=False, encoding='utf8')
x = data['Situps'].as_matrix().reshape(len(data['Situps']), 1)
y = data['Jumps']

trainX, testX = train_test_split(x, shuffle=False)
trainY, testY = train_test_split(y, shuffle=False)

model = linear_model.LinearRegression()
model.fit(trainX, trainY)
pred = model.predict(testX)
plt.scatter(x, y, color='black')
plt.plot(testX, pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()