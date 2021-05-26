import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = pd.read_csv("business-financial-data-dec-2020-quarter-CSV.csv")
# print(data.head())
# print(data.columns)
# print(data.tail(3))
# print(data['Data_value'])

# plt.matshow(data.corr())
# plt.show()

plt.xticks(range(data.shape[1]), data.columns, fontsize=12, rotation=90)
plt.yticks(range(data.shape[1]), data.columns, fontsize=12)
plt.show()

# y = data['Suppressed']
# X = data['Data_value']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(model.predict([24]))
# print(model.predict([660]))
# print(model.predict([[24.12, 26, 0.1]]))
# print(accuracy_score(y_pred, y_test))
# print(mean_squared_error(y_test, y_pred))