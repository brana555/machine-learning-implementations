import numpy as np
import matplotlib.pyplot as plt
import mnist_reader
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


# import some data to play with
X_train, y_train = mnist_reader.load_mnist('data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist('data/fashion', kind='t10k')

rfc = RandomForestClassifier()

rfc.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = rfc.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))