# 
# created by alex mounsey

# import modules
from preprocessing import preprocess

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve

from keras.models import Sequential
from keras.layers import Dense

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib

# import and preprocess dataset
dataset = pd.read_csv('diabetes.csv')
dataset = preprocess(dataset)

# split dataset into input features and target variables
inputFeatures = dataset.loc[:, dataset.columns != 'Outcome']
targetVariable = dataset.loc[:, 'Outcome']
# split data into training (80%) and testing (20%)
xTrain, xTest, yTrain, yTest = train_test_split(inputFeatures, targetVariable, test_size=0.2)
# further split training split into training (80%) and validation (20%)
xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size=0.2)