# Simple Linear Regression

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd


# Import the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values # 2D array: Removing last column (salary). only years of experience will remain
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
 
# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# scX = StandardScaler()
# xTrain = scX.fit_transform(xTrain)
# xTest = scX.transform(xTest)


# Fitting Simple Linear Reqression  to training set
from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(X_train, y_train) 

# Predicting the Test set results
y_pred = regressor.predict(X_test)

yy_pred = regressor.predict([[1], [2], [3], [4], [5]]) # custom input

# Visulalizing the training set
plt.scatter(X_train, y_train, color='red')  # Observation points
plt.plot(X_train, regressor.predict(X_train), color='blue')  # Regression line 
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Visulalizing the test set
plt.scatter(X_test, y_test, color='red')  # Observation points

plt.plot(X_train, regressor.predict(X_train), color='blue')  # Regression line remain same as above

plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
