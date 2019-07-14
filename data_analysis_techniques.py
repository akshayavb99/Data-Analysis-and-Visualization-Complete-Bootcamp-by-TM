import pandas as pd
import numpy as np

from pandas import Series, DataFrame
from numpy import random

#--------- DATA ANALYSIS TECHNIQUES AND METHODOLOGIES ----------#

#---------- MERGING DATAFRaMES (COLUMNWISE MERGING) -------------#

#1. Many to one merging

dframe1=DataFrame({'reference':['ola','uber','lyft','gojek','grab'],'revenue':[1,2,3,4,5]})
dframe2=DataFrame({'reference':['ola','uber','uber','ola'],'revenue':[1,2,3,4]})

#merge() function compares the index values of the 2 argument dataframes and only includes the common indices for the new dataframe.
df3=pd.merge(dframe1,dframe2)
print(df3)
print()

df3=pd.merge(dframe1,dframe2,on='reference') #This merges dataframes based on the reference parameter. In the output revenue_x is for values from dframe1 and revenue_y from dframe2
print(df3)
print()

#how parameter in merge() offers a variety of argument values.
#(i) left = Considers all datavalues in dframe1 for d4 s seperate values even if there are repetitions in dframe2
#(ii) right = Considers all datavalues in dframe2 for d4 as seperate values even if there are repetitions in dframe1
#(iii) outer = Takes the union of reference parameter from dframe1 and dframe2
df4=pd.merge(dframe1,dframe2,on='reference',how='left')
print(df4)
print()

#2. Many to Many Merging
df6=DataFrame({'reference':['ola','ola','lyft','lyft','uber','uber','ola'],'revenue':[1,2,3,4,5,6,7]})
df7=DataFrame({'reference':['uber','uber','lyft','ola','ola'],'revenue':[1,2,3,4,5]})
print(pd.merge(df6,df7))
print()

#3.Multiple References
df8=DataFrame({'reference':['ola','ola','lyft'],'revenue':['one','two','three'],'profit':[1,2,3]})
df9=DataFrame({'reference':['ola','ola','lyft','lyft'],'revenue':['one','one','one','three'],'profit':[4,5,6,7]})
print(pd.merge(df8,df9,on=['reference','revenue'],how='outer',suffixes=('_first','_second')))

#-------- NEXT LECTURE --------#

#Merging using Indices (Row-wise)

df_1=DataFrame({'reference':['O','U','L','O','U'],'data':range(5)})
df_2=DataFrame({'profit':[10,20]},index=list('OU'))

print(pd.merge(df_1,df_2,left_on='reference',right_index=True))
print()
#left_on = Parameter for merging the dataframes
#right_index = To set the merging criteria of 2nd dataframe as the index

df_3=DataFrame({'ref1':['A','A','O','O','A'],'ref2':[5,10,15,20,25],'ref3':[0,1,2,3,4]})
df_4=DataFrame(np.arange(10).reshape(5,2),index=[['A','A','O','O','O'],[20,10,10,10,20]],columns=['col1','col2'])
print(pd.merge(df_3,df_4,left_on=['ref1','ref2'],right_index=True))

#Merge is time-consuming with complicated arguments, hence join() function is preferred
#join() - Research more. The dimensions of the DataFrame rows and columns must be same else it throws an error


#---------- NEXT LECTURE ----------#

#Concatenation of Datasets

B1=np.arange(25).reshape(5,5)
A1=np.random.randn(25).reshape(5,5)
print(np.concatenate([A1,B1],axis=0)) #axis=1 means concatenation along column
print()

#In Pandas Series using concat() function
s1=Series([100,200,300],index=['A','B','C'])
s2=Series([400,500],index=['D','E'])
print(pd.concat([s1,s2],axis=1))

#Pandas DataFrames

df1=DataFrame(random.randn(4,3),columns=['A','B','C'])
df2=DataFrame(random.randn(3,3),columns=['B','D','A'])
print(pd.concat([df1,df2],sort=True,ignore_index=True))
print()

#------- NEXT LECTURE --------#

#Combining Dataframes

s1 = Series([5,np.nan,6,np.nan], index=['A','B','C','D'])
s2 = Series(np.arange(4), dtype=np.float64, index=s1.index)
s3 = Series(np.where(pd.isnull(s1),s2,s1),index=s1.index)
s4 = s1.combine_first(s2)

#Dataframes

df_5m = DataFrame({ 'col1': [5,np.nan,15],'col2': [20,25,np.nan],'col3':[np.nan,np.nan,35]})
df_10m = DataFrame({ 'col1': [0,10,20],'col2': [10,20,30]})
#combine_with() in dataframes - Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame. The row and column indexes of the resulting DataFrame will be the union of the two.
print(df_5m.combine_first(df_10m))
print()

#---------- NEXT LECTURE ---------#

#Reshaping Dataframes - Stacking and Unstacking of Dataframes

df1 = DataFrame(np.arange(8).reshape(2,4), index=pd.Index(['Uber','Grab'],name="cabs"), columns=pd.Index(['c1','c2','c3','c4'],name="attributes"))
#print(df1)

#stack() creates a Series from the calling dataframe
stack_df1=df1.stack()
print(stack_df1)

#unstack() performs opposite of the stack() function
unstack_df1=stack_df1.unstack()
print(unstack_df1)
print()

#Unstacking along different attributes (Along index or column values)
df3=stack_df1.unstack('cabs')
#print(df3)
df4 = stack_df1.unstack('attributes')
#print(df4)

#stack() and unstack() in Series
s1 = Series([5,10,15],index=['A','B','C'])
s2 = Series([15,20,25],index=['B','C','D'])

s3 = pd.concat([s1,s2],keys=['k1','k2'])
#print(s3)

df = s3.unstack()
print(df.stack())
print()
print(df.stack(dropna=False))

#----------- NEXT LECTURE ---------#

#Pivot Tables

url = "https://en.wikipedia.org/wiki/Pivot_table"
df_list = pd.io.html.read_html(url)
df = df_list[0]

print(df)

new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
print()


#print(df)
#Creating a pivot table

#print (df.pivot('Date of sale', 'Sales person', 'Total price'))

#---------- NEXT LECTURE --------#

#Duplicates Analysis in Datasets
df = DataFrame({'col1':['uber','uber','uber','uber','grab'],'col2':[5,4,3,3,5]})
print(df)
print (df.duplicated()) #Returns a list of boolean values to find duplicate values in the array

print (df.drop_duplicates())

print (df.drop_duplicates(['col1']))

print (df.drop_duplicates(['col1'] , keep='last')) #take_last parameter is deprecated, use keep parameter instead
print()

#--------- NEXT LECTURE ---------#

#Mapping in Dataframes - Used for data cleaning and element-wise transformation in dataframes

df = DataFrame({ 'country': ['Afghanistan','Albania','Algeria'],'code':['93','355','213']})
GDP_map = {'Afghanistan': '20', 'Albania': '12.8','Algeria':'215'}
df['GDP'] = df['country'].map(GDP_map) #A new column in df is created with name 'GDP', where the values are mapped to the dictionary values in GDP_map

print(df)
print()

#-------- NEXT LECTURE --------#

#Replacing values in Series

s1 = Series([10,20,40,50,20,10,50,40])
print (s1)

#replace(num1,num2) function replaces num1 with num2.
print (s1.replace(50,np.nan))

#In the statement below, each element of 1st list of values is replaced by the corresponding element of the 2nd list of values
print (s1.replace([10,20,50],[100,200,500]))

#Thi uses a dictionary for replacement - 10 with 100, 20 with null, 40 with 400
print (s1.replace({10:100,20:np.nan,40:400}))
print()

#----------- NEXT LECTURE ---------#

#Renaming indexes
df = DataFrame(np.arange(25).reshape(5,5), index=['UBER','OLA','GRAB','GOJEK','LYFT'], columns=['RE','LO','QU','GR','AG'])
print (df)

#way1 -  use mapping
df.index = df.index.map(str.lower)
print (df)

#way2 - rename method - Here, the original dataframe df is not affected
print (df.rename(index=str.title,columns=str.lower))

#way3 of using dictionary
print (df.rename(index={'uber':'The Best Taxi'}, columns={'RE':'Revenue'}))

#how to save
df.rename(index={'uber':'The Best Taxi'}, columns={'RE':'Revenue'},inplace=True) #inplace parameter = True means that the changes through rename() are reflected in original dataframe df
#print (df)
print()

#--------- NEXT LECTURE --------#

#Binning values - Seperateing values in categories

prime_nos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
number_bins = [0,10,20,30,40,50]

#cut() function seperates the values of prime_nos into categories (ranges) as per the number_bins like 0-10, 10-20, 20-30, 30-40, 40-50
category = pd.cut(prime_nos,number_bins)
print (category)
print()

#categories parameter in the category gives greater detail about category like the intervals of each category.
print (category.categories)
print()

#value_counts - The parameter returns the number of values in each category
print (pd.value_counts(category))
print()

#limits - Define the number of bins (Categories) you want to create using the precision parameter and the 2nd argument.
print (pd.cut(prime_nos,3,precision=1))
print()

#--------- NEXT LECTURE ---------#

#Observations on a dataframe - what you do when given a dataframe - initial view
df = DataFrame(np.random.randn(1000,5))

#basic observation
print (df.head()) #Returns the top 5 rows including dataframe header
print (df.tail()) #Returns the last 5 rows

print (df.describe()) #Gives basic statistical info about the data of the dataframe

column = df[0]
print (column.head())
print()
print (column[np.abs(column)>3])
print()

print (df([(np.abs(df)>3).any(1)]))

df[(np.abs(df)>3)] = np.sign(df)*5

#print (df.describe())


