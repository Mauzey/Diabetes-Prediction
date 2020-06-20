# Diabetes-Prediction
A multi-layer perceptron which predicts whether an individual is susceptible to diabetes. The model will be trained on the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database), provided by the National Institute of Diabetes and Digestive and Kidney Diseases.

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
* Variables are on different scales, and therefore must be standardised
* The majority of data has been collected from individuals between 20 and 30 years of age
* BMI, Blood Pressure, and Glucose Concentration are normally distributed
  * This is to be expected when such statistics are collected from a population
* It is impossible for for BMI, Blood Pressure, and Glucose Concentration to have a value of zero
  * Missing or incomplete data?
* Certain individuals have had up to 15 pregnancies
  * While not implausible, this information should still be considered
* This data-set suggests that 35% of the population has diabetes (65% do not)
  * The World Health Organisation estimates that only 8.5% of the global population suffers from diabetes
  * ...this data-set is therefore not representative of the global population, which is to be expected due to its nature

### Density Plots
![Pima Indians Diabetes Database Density Plots](https://i.imgur.com/KxzKKTu.png)

#### Insights
* Glucose Concentration, BMI, and Age appear to be the strongest predicting values for those with diabetes
* Blood Pressure and Skin Thickness do not appear to have a significant correlation with the distribution of diabetic and non-diabetic individuals
