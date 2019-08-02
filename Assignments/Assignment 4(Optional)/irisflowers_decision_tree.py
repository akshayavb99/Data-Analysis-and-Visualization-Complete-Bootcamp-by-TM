#Making a decision tree with Iris Dataset using C5.0 model training
#Reference: https://medium.com/@haydar_ai/learning-data-science-day-21-decision-tree-on-iris-dataset-267f3219a7fa

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series,DataFrame

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris_data=pd.read_csv('D:\PycharmProjects\Python Practice\Iris.csv')
'''print(iris_data)

#print(iris_data.isnull().any()) #- See if there are any null values
#print(iris_data.dtypes) #- See the data types of each column
#print(iris_data.describe()) #-Quick summary of data Check for any drastic variations in column values

iris_data['PetalWidthCm'].plot.hist()
plt.show()'''

#Forming a test and training set since we have only one dataset.
all_inputs = iris_data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
all_classes = iris_data['Species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

dtc = DecisionTreeClassifier()
print(dtc.fit(train_inputs, train_classes))
print(dtc.score(test_inputs, test_classes))

