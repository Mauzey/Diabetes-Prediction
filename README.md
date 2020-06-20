# Diabetes-Prediction
A multi-layer perceptron which predicts whether an individual is susceptible to diabetes. The model has been trained on the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database), provided by the National Institute of Diabetes and Digestive and Kidney Diseases.

## Libraries Used
```matplotlib```
```pandas```
```Keras```
```NumPy```
```seaborn```
```scikit-learn```

## Data Analysis
### Histograms
![Pima Indians Diabetes Database Histograms](https://i.imgur.com/8EtFIWH.png)
*Note: 'outcome' refers to whether an individual does, or does not, have diabetes*

#### Insights
* Variables are on different scales, and therefore must be standardized
* The majority of data has been collected from individuals between 20 and 30 years of age
* ```BMI```, ```Blood Pressure```, and ```Glucose``` are normally distributed
  * This is to be expected when such statistics are collected from a population
* It is impossible for for ```BMI```, ```Blood Pressure```, and ```Glucose``` to have a value of zero
  * Missing or incomplete data?
* Certain individuals have had up to 15 pregnancies
  * While not implausible, this information should still be considered
* This data-set suggests that 35% of the population has diabetes (65% do not)
  * The World Health Organisation estimates that only 8.5% of the global population suffers from diabetes
  * ...this data-set is therefore not representative of the global population, which is to be expected due to its nature

### Density Plots
![Pima Indians Diabetes Database Density Plots](https://i.imgur.com/KxzKKTu.png)

#### Insights
* ```Glucose```, ```BMI```, and ```Age``` appear to be the strongest predicting values for those with diabetes
* ```Blood Pressure``` and ```Skin Thickness``` do not appear to have a significant correlation with the distribution of diabetic and non-diabetic individuals

## Data Pre-Processing
### Missing or Incomplete Values
#### Statistical Summary
![Pima Indians Diabetes Database Statistical Summary](https://i.imgur.com/yZN89GB.png)
* There are a total of 768 entries
* ```Pregnancies```, ```Glucose Concentration```, ```Blood Pressure```, ```Skin Thickness```, ```Insulin```, and ```BMI``` appear to have a minimum value of zero. This indicates missing values as such values are impossible

#### Number of Missing Values
![Pima Indians Diabetes Database No. of Missing Values](https://i.imgur.com/Q7meZol.png)
* There is a significant number of missing values. Most notably, a large number of entries for ```Insulin``` and ```Skin Thickness``` are missing
* Due to the fact that missing values have been determined by searching for entries with a value of zero, ```Pregnancies``` can be ignored as an individual with zero pregnancies is perfectly valid
* Missing values have been replaced with the mean of non-missing values

### Data Standardization
#### Statistical Summary of Standardized Data
![Pima Indians Diabetes Database Standardized Summary](https://i.imgur.com/N77tBkx.png)
* The values for ```Outcome``` have been copied from the original dataset as they do not require standardization
