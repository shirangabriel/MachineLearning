# Data Preprocessing

# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


# Import the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
 
# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# scX = StandardScaler()
# xTrain = scX.fit_transform(xTrain)
# xTest = scX.transform(xTest)






















