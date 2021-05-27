import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('iris.csv')
print(df.shape)
print(df.tail(2))
print(df.columns)
print(df[['sepal_length', 'sepal_width']].head(3))
#
# le = LabelEncoder()
# df["species"] = le.fit_transform(df["species"])
# X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
# y = df["species"]
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
# model = Sequential()
#
# model.add(Dense(8, activation='relu', input_shape=(4,)))
# model.add(Dense(3, activation='relu'))
# model.add(Dense(1, activation='softmax'))
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)
#
# from sklearn import metrics
#
# yPredicted = model.predict(X_test)
#
# print(metrics.accuracy_score(y_test, yPredicted))