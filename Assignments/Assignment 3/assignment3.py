#Problem Statement:
#Create a HeatMap Plot for the following plot with Seaborn:
#1. Download the DataSet from the GitHub link: https: // raw.githubusercontent.com / resbaz / r - novice - gapminder - files / master / data / gapminder - FiveYearData.csv to solve this problem.
#The dataset has 5 columns namely: country, year, pop, continent, lifeExp and gdpPercap
#2. Create a pivot table dataframe with year along x-axes, continent along y-axes and lifeExp filled within cells.
#3. Plot a heatmap using seaborn for the pivot table that was just created.

import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('D:\PycharmProjects\Python Practice\gapminder-FiveYearData.csv')
#print(df)

#Checking for data duplication and NaN values
df['is-duplicate']=df.duplicated()
df=df.dropna(how='all')
#print(df)

#Creating the pivot table
pvt_tbl=df.pivot('year','country','lifeExp')
print(pvt_tbl)

#Creating heatmap using seaborn
fig=sns.heatmap(pvt_tbl,fmt="",cmap='RdYlGn',linewidth=0.1).get_figure().savefig('assignment_output.png')
plt.show()
