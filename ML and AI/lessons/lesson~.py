import pandas
data = pandas.read_csv('wine.csv')
# print(data.head(3))
# print(data.tail(3))
# print(data.columns)
# print(data['Alcohol'])
# print(data['Alcohol'].head(3))
# print(data[['Wine', 'Alcohol']].tail(2))
# print(data.iloc[0, 1]) loc
# print(data.shape)
# print(data.info())
# print(data.describe())

import matplotlib.pyplot as plt
# plt.matshow(data.corr())
# plt.xticks(range(data.shape[1]), data.columns, fontsize=12, rotation=90)
# plt.yticks(range(data.shape[1]), data.columns, fontsize=12)
# cb = plt.colorbar()
# cb.ax.tick_params(labelsize=12)
# plt.show()


# data.hist()
# plt.show()

import seaborn
# seaborn.countplot(data['Wine'])
# plt.show()

y = data['Wine']
X = data[['Ash', 'Phenols', 'Hue']]

# from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 20)

model.fit(Xtrain, ytrain)

from sklearn import metrics

yPredicted = model.predict(Xtest)

print(metrics.accuracy_score(ytest, yPredicted))