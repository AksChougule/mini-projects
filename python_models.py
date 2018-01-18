__author__ = 'Akshay Chougule'

## Basic classifer programm using sklearn
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

# Feature set
features = [[140,0],
            [130,0],
            [150,1],
            [170,1]]

# Labels
labels = ["apple","apple","orange","orange"]

# Decision tree algorithm
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[160,1]])

# Naive bayes
gnb = GaussianNB()
clf = gnb.fit(features,labels)
print clf.predict([[160,1]])
