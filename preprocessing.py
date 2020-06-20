# preprocessing dataset
# created by alex mounsey

# import modules
from sklearn import preprocessing
import pandas as pd
import numpy as np

def preprocess(dataset):
    # check for missing values
    print("Missing Values:")
    print("---------------")
    print(dataset.isnull().any())
    print("")

    # print statistical summary of the dataset
    print("Statistical Summary:")
    print("--------------------")
    print(dataset.describe())
    print("")

    # print the number of missing values within the dataset
    print("Number of Missing Values:")
    print("-------------------------")
    for col in dataset.columns:
        missing_row = dataset.loc[dataset[col] == 0].shape[0]
        print(col + ": " + str(missing_row))
    print("")

    # replace missing values with 'NaN'
    print("Replacing values of '0' with 'NaN'...")
    dataset['Glucose'] = dataset['Glucose'].replace(0, np.NaN)
    dataset['BloodPressure'] = dataset['BloodPressure'].replace(0, np.NaN)
    dataset['SkinThickness'] = dataset['SkinThickness'].replace(0, np.NaN)
    dataset['Insulin'] = dataset['Insulin'].replace(0, np.NaN)
    dataset['BMI'] = dataset['BMI'].replace(0, np.NaN)
    print("")

    # confirm that these columns no longer have values of zero
    print("Number of Entries Equal to Zero:")
    print("--------------------------------")
    for col in dataset.columns:
        missing_row = dataset.loc[dataset[col] == 0].shape[0]
        print(col + ": " + str(missing_row))

    # replace 'NaN' values with the mean of non-missing values
    print("Replacing 'NaN' values with the mean of non-missing values...")
    dataset['Glucose'] = dataset['Glucose'].fillna(dataset['Glucose'].mean())
    dataset['BloodPressure'] = dataset['BloodPressure'].fillna(dataset['BloodPressure'].mean())
    dataset['SkinThickness'] = dataset['SkinThickness'].fillna(dataset['SkinThickness'].mean())
    dataset['Insulin'] = dataset['Insulin'].fillna(dataset['Insulin'].mean())
    dataset['BMI'] = dataset['BMI'].fillna(dataset['BMI'].mean())
    print("")


    # data standardization
    print("Standardizing Data...")
    datasetScaled = preprocessing.scale(dataset) # scale dataset
    datasetScaled = pd.DataFrame(datasetScaled, columns=dataset.columns) # convert scaled dataset to pandas dataframe
    datasetScaled['Outcome'] = dataset['Outcome'] # copy outcome column from original dataset
    dataset = datasetScaled
    print("")

    # print statistical summary of the standardized dataset
    print("Standardized Dataset Summary:")
    print("-----------------------------")
    print(dataset.describe().loc[['mean', 'std', 'max'],].round(2).abs())
    print()

    return dataset