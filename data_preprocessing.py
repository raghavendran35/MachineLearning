# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #everything but the last
y = dataset.iloc[:,3].values

#take care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN",strategy = "mean", axis = 0) #default value of strategy is mean
#axis is 0 
imputer = imputer.fit(X[:,1:3]) #columns one and two are the messed up data columns
X[:,1:3] = imputer.transform(X[:,1:3]) #replace the columns of X with the trandformed imputer object

#Now need to encode our variables, country and purchased
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])    #column values is :, and then index


#new smart way: create dummy variables-- 3 columns for our first categorical variable (France, Germany, Spain)
#i.e. thing with france in it would have values 1, 0, 0 for its first three columns
onehotencoder = OneHotEncoder(categorical_features = [0])  #first column should be encoded
X = onehotencoder.fit_transform(X).toarray()

#For Y values, purchased or not becomes 1 or 0
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) 


#split our dataset into training and test set, just for validation, validate YOUR OWN DATA!!!!!, do not want toooo much data because that may not deliver the logic
#HELPS MAKES SURE WE DO NOT OVERFIT
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2,train_size = 0.8,random_state = 0)


#feature scaling due to large euclidean distance between poitns (values with larger ranges can be issues)

#change Age and Salary columns from -1 to 1--can stanadardize or normalize
#note standardize is with creating Z-scores!!!
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train) #take test set, fit then transform
X_test = sc_X.transform(X_test) #take test set, fit then transform

#feature scaling to dummy variables depends
#feature scaling to y variable is not needed because we are dealing with categorical variables!!!


