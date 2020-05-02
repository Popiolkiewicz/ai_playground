from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import numpy as np

# X = [[1,2],[2,1],[3,1],[4,1],[5,3],[6,2],[7,1],[8,4],[9,1],[10,1]]
# y = [2,3,4,5,6,7,8,9,10,11]

X = np.arange(100).reshape((50,2))
y = list(range(0,10)) + list(range(40,80))

print(X)
print(y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.05)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)