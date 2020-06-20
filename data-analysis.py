# exploratory data analysis
# created by alex mounsey

# import modules
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# import dataset
dataset = pd.read_csv('diabetes.csv')

# print first few rows of the dataset
print(dataset.head())

# plot histogram
dataset.hist()
plt.show()

# create 3x3 subplot
plt.subplots(3, 3, figsize=(15,15))

# plot density plot for each variable
for idx, col in enumerate(dataset.columns):
    ax = plt.subplot(3, 3, idx + 1)
    ax.yaxis.set_ticklabels([])

    sns.distplot(dataset.loc[dataset.Outcome == 0][col], hist=False, axlabel=False, kde_kws={'linestyle':'-', 'color':'black', 'label':"No Diabetes"})
    sns.distplot(dataset.loc[dataset.Outcome == 1][col], hist=False, axlabel=False, kde_kws={'linestyle':'--', 'color':'black', 'label':"Diabetes"})

    ax.set_title(col)

# hide nith subplot
plt.subplot(3, 3, 9).set_visible(False)

plt.show()