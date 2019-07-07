import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To work with the Series functionality of Pandas Library
from pandas import Series, DataFrame

obj=Series([5,10,15,20]) #1. Series are modifiable.
print(obj)

#To print the values without the indices, use the values attribute of obj
print(obj.values)

#index is another attribute of the Series object that stores only the index values for the Series object
print(obj.index)
print()

#2. How to use numpy arrays to create Series
data_arr=np.array(['a','b','c'])
arr_obj=Series(data_arr)
print(arr_obj)
print()

#3. Using custom index values in Series
s=Series(data_arr,index=[100,101,102])
print(s)
print()
#Indices can be strings as well
s=Series(data_arr,index=['index1','index2','index3'])
print(s)
print()

#4. Real Life Example

#The revenue Series object stores the revenues of the companies given as index values in billions
revenue=Series([20,80,40,35],index=['Ola','Uber','Grab','Gojek'])
print(revenue)
print("Revenue of Ola: "+str(revenue['Ola']))
print()

#(i)Revenue of companies > 35
print("Revenue of companies >= 35: ")
print(str(revenue[revenue>=35]))
print()

#(ii) Using Boolean Conditions in Series
print("Is lyft in the data?: "+str('lyft' in  revenue))
print()

#(iii) Conversion of Series into dictionary
revenue_dict=revenue.to_dict() #Converts the series into a dictionary with key-value pairs where key=index
print(revenue_dict)
print()

#(iv) Handling NaN values (important for situations where data is missing during data analysis
index_2=['Ola','Uber','Grab','Gojek','Lyft']
revenue2=Series(revenue,index_2)
print(revenue2) #Revenue value of 'Lyft' index is automatically taken as NaN since no value was defined
print(pd.isnull(revenue2)) #Only the value corresponding to index 'Lyft' is True due to the NaN revenue value
print()

#(v) Opposite function of pd.isnull(Series obj)
print(pd.notnull(revenue2))
print()

#5. Addition of series
print(revenue+revenue2) #Here the final result is printed in the ascending order of the index values (Here, alphabetically)
print()

#6. Assigning names
revenue2.name="Company Revenues" #Essentially a title for the Series
revenue2.index.name="Company Names" #Title for index values
print(revenue2)
print()

#-------------- NEXT LECTURE ----------#

#Dataframes in Pandas
#Dataframe is a matrix with rows and columns with index and column names

#1. Example of revenue analysis from a table

#revenue_df=pd.read_clipboard() #This automatically loads the data last copied into revenue_df

#For the current table values being copied from Wikipedia there is an error that shows up with the command above.
#To go past this, save the required rows as a CSV file and use the read_csv() function with the seperator as '\t'
#revenue_df = pd.read_clipboard()
#print(revenue_df)


#---------- NEXT LECTURE ----------#

#Indexing in Pandas

series1=Series([10,20,30,40],index=['a','b','c','d'])
print(series1)
print()

#Index property of Series
index1=series1.index
print(index1[2])
print(index1[2:])

#Negative indices
print(index1[-1:]) #This displays only the last element from the array index1. This is essentially indexing the array in reverse

#Important concepts

#1. When you are dealing with a DataFrame, we cannot assign a new value to the indices of the DataFrame with the assignment operator
#   Following statement throws an error.

#index1[0]='e'
print(index1)
print()

#---------- NEXT LECTURE --------#

#Reindexing methods

series1=Series([1,2,3,4],index=['e','f','g','h'])
print(series1)

#1. Creating new indices using reindex function
series2=series1.reindex(['e','f','g','h','i','j'])
print(series2)
print()

series2=series2.reindex(['e','f','g','h','i','j','k'],fill_value=10)
print(series2)
print()

#2.Reindexing using ffill

cars=Series(['Audi','Merc','BMW'],index=[0,4,8])
ranger=range(13) #Creates a list of elements from 0 to 12 (both inclusive)
cars=cars.reindex(ranger,method="ffill")

#ffill ensures that indices from 0 to 3 has value Audi, 4 to 7 have value Merc and so on.
print(cars)
print()

#3. Creating a new dataframe using randn
df_1=DataFrame(np.random.randn(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df_1)
print()

df_2=df_1.reindex(['a','b','c','d','e','f']) #Reindexing Rows
print(df_2)
print()

df_3=df_1.reindex(columns=['c1','c2','c3','c4','c5','c6'])
print(df_3)
print()

#4. Using .ix[] for reindexing - .ix[] allows the reindexing of both rows and colummns simultaneously. However, .ix[] has been
#   depreceated in favor of .iloc and .loc indexers (Source: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated)
#df_4=df_1.ix(['a','b','c','d','e','f'],['c1','c2','c3','c4','c5','c6'])
#print(df_4)
#print()

#------------ NEXT LECTURE ----------#

#Dropping entries from datatypes
cars=Series(['BMW','Audi','Merc'],index=['a','b','c'])

#Using drop(idx) function, we can remove a value from the Series object from the index idx
cars=cars.drop('a')

#Dataframes
cars_df=DataFrame(np.random.randn(9).reshape(3,3),index=['BMW','Audi','Merc'],columns=['rev','pro','exp'])
print(cars_df) #Current values in the matrix of the dataframe are random values
print()

#Dropping row values
cars_df=cars_df.drop('BMW',axis=0)#Drops the index 'BMW' (The row given as 'BMW')

#Dropping column values. To perform operations on the columns, we need to explicitly set the axis as 1
cars_df=cars_df.drop('pro',axis=1)

#---------- NEXT LECTURE -----------#

#Handling null data in pandas
series1=Series(['A','B','C','D',np.nan]) #np.nan is essentially null
print(series1)

#1. Validation of null statements using function isnull().
#isnull() returns true if the passed value(s) is/are null
print(series1.isnull())
print()

#2. Dropping null values
print(series1.dropna())
print()

df1=DataFrame([[1,2,3],[5,6,np.nan],[7,np.nan,10],[np.nan,np.nan,np.nan]])
#When we use the dropna() function, the whole row is dropped even if there is one row element=NaN.
#To overcome this problem, we can set the how property within the dropna() function as 'all'
print(df1.dropna(how='all'))

#Column wise dropping null values
print(df1.dropna(axis=1)) #The dropna() works similar in row and column NaN value drops
print()

#Threshold property of dropna() [thresh]
df2=DataFrame([[1,2,3,np.nan],[4,5,6,7],[8,9,np.nan,np.nan],[12,np.nan,np.nan,np.nan]])
print(df2.dropna(thresh=3)) #This drops all rows where number of data values (not equal to NaN) is lesser than 3

#3. Filling NaN values with chosen numerical values - fillna() function
print(df2.fillna({0:0,1:50,2:100,3:200}))
print()

#----------- NEXT LECTURE -------------#

#Selecting and modifying data in pandas
series1=Series([100,200,300],index=['a','b','c'])
#The Series always have in-built indices of 0,1,2.... even if we explicitly mention other indices. Hence we can access
#the series elements by the in-built indicies as well

#Conditional Indexing
print(series1[series1>150])
print(series1[series1==300])

df1=DataFrame(np.arange(9).reshape(3,3),index=['car','bike','cycle'],columns=['A','B','C'])
print(df1[['A','B']]) #Printing Multiple Columns

print(df1>5) # Returns a matrix of dimensions of df1 where each element is a boolean value whose is result is the condition mentioned
print()

#Using ix to access elements - Note that ix is deprecated and it is preferable to use .iloc and .loc indexers.

#print(df1.ix['bike']) #ix is primarily is used for row-wise access

#---------- NEXT LECTURE -----------#

#Data Alignment and Regulation

ser_a=Series([100,200,300],index=['a','b','c'])
ser_b=Series([300,400,500,600],index=['a','b','c','d'])

#Sum of series = ser_a+ser_b
print(ser_a+ser_b)

#Dataframes
df1=DataFrame(np.arange(4).reshape(2,2),columns=['a','b'],index=['car','bike'])
df2=DataFrame(np.arange(9).reshape(3,3),columns=['a','b','c'],index=['car','bike','cycle'])
print(df1+df2) #All the elements of 3 index and 3rd column are not available in df1 hence the NaN value after summation
#To bypass the NaN, use the add function with a fill_value of 0 for all undefined rows/columns
print(df1.add(df2,fill_value=0))
print()

#---------- NEXT LECTURE -----------#

#Ranking and Sorting

ser1=Series([500,1000,1500],index=['a','c','b'])
#Sorting by index using sort_index()
print(ser1.sort_index())

#Sorting by values using sort_values()
print(ser1.sort_values())

#rank() function - Prints the ranking value after they are sorted in ascending order
print(ser1.rank())

#Ranking of Series (Basis for Sorting)
ser2=Series(np.random.randn(4))
print(ser2.rank())
print()

#--------------- NEXT LECTURE -------------#

#Statistics in Pandas
arr1=np.array([[10,np.nan,20],[30,40,np.nan]])
df1=DataFrame(arr1,index=[1,2],columns=list('ABC'))

#1. sum() - performs summation along each column. Set axis=1 for summation along indexes(rows) NaN is considered as 0
print(df1.sum())
print(df1.sum(axis=1))
print()

#2. min()/max() - returns minimum/maximum values along the columns.
print(df1.max())
print()

#3. idxmax()/idxmin() - returns the index of the maximum/minimum values along the columns
print(df1.idxmax())
print()

#4. cumsum() -returns cumulative sum along the columns.NaN is considered as 0
print(df1.cumsum())
print()

#5. describe() - Shows the overall stats table for the given data column-wise
print(df1.describe())
print()

#Graphs and Statistics
df2=DataFrame(np.random.randn(9).reshape(3,3),index=[1,2,3],columns=list('ABC'))

#Plotting values column-wise against indices
plt.plot(df2)
plt.legend(df2.columns,loc='lower right')
plt.savefig('df2_plot1.png')
#plt.show()
print()

#unique() - returns the unique values in the Series
ser1=Series(list('abcccaabd'))
print(ser1.unique())

#value_counts() - returns the frequency of element occurence in series in descending order
print(ser1.value_counts())