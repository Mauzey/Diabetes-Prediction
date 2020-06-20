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
print("Splitting dataset...")
inputFeatures = dataset.loc[:, dataset.columns != 'Outcome']
targetVariable = dataset.loc[:, 'Outcome']
# split data into training (80%) and testing (20%)
xTrain, xTest, yTrain, yTest = train_test_split(inputFeatures, targetVariable, test_size=0.2)
# further split training split into training (80%) and validation (20%)
xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size=0.2)
print("")

# define neural network structure
print("Building model...")
model = Sequential()
# first hidden layer consists of 32 nodes. The input dimensions are 8 due to there being 8 columns in the training data
model.add(Dense(32, activation='relu', input_dim=8))
# the second hidden layer consists of 16 nodes
model.add(Dense(16, activation='relu'))
# the output layer consists of a single node as we are dealing with binary classification
# the sigmoid activation function 'squashes' the output between 0 and 1
model.add(Dense(1, activation='sigmoid'))
print("")

# compile and train the model
print("Compiling and training model...")
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(xTrain, yTrain, epochs=200, verbose=False)
print("")

# accuracy results
print("Results:")
print("--------")
scores = model.evaluate(xTrain, yTrain, verbose=False)
print("Training Accuracy: %.2f%%\n" % (scores[1] * 100))
scores = model.evaluate(xTest, yTest, verbose=False)
print("Testing Accuracy: %.2f%%\n" % (scores[1] * 100))

# confusion matrix
yTestPredict = model.predict_classes(xTest)
cMatrix = confusion_matrix(yTest, yTestPredict)

ax = sns.heatmap(cMatrix, annot=True, xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['NoDiabetes', 'Diabetes'], cbar=False, cmap='Blues')
ax.set_xlabel("Predicted Value")
ax.set_ylabel("Actual Value")

plt.show()
plt.clf()

# ROC curve
yTestPredictProbability = model.predict(xTest)
FPR, TPR, _ = roc_curve(yTest, yTestPredictProbability)

plt.plot(FPR, TPR)
plt.plot([0,1], [0,1], '--', color='black')
plt.title('ROC Curve')
plt.xlabel('False-Positive Rate')
plt.ylabel('True-Positive Rate')

plt.show()
plt.clf()