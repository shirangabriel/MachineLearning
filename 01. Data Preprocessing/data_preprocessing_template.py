# Data Preprocessing# Importing the librariesimport numpy as np import matplotlib.pyplot as pltimport pandas as pd# Import the datasetdataset = pd.read_csv('Data.csv')x = dataset.iloc[:, :-1].valuesy = dataset.iloc[:, 3].values# Taking care missing datafrom sklearn.impute import SimpleImputerimputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')imputer = imputer.fit(x[:, 1:3])x[:, 1:3] = imputer.transform(x[:, 1:3])# Encoding categorical datafrom sklearn.preprocessing import LabelEncoder, OneHotEncoderlabelEncoderX  = LabelEncoder()x[:, 0] = labelEncoderX.fit_transform(x[:, 0]) from sklearn.compose import ColumnTransformertransformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])],remainder='passthrough')x = np.array(transformer.fit_transform(x), dtype=np.float)labelEncoderY  = LabelEncoder()y = labelEncoderX.fit_transform(y) # Splitting the dataset into the Training set and Test setfrom sklearn.model_selection import train_test_splitxTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0) # Feature Scalingfrom sklearn.preprocessing import StandardScalerscX = StandardScaler()xTrain = scX.fit_transform(xTrain)xTest = scX.transform(xTest)