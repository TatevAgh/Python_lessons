import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv('iris.csv')
print(data.columns)

y = data['species']
X = data['sepal_length', 'sepal_width', 'petal_length']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))

