# Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the data set
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(
 #   X, y, test_size=1/3, random_state=0)
