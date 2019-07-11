#--------- FILE OPERATIONS IN PYTHON ----------#

import numpy as np
import pandas as pd
from pandas import Series,DataFrame,read_html

#For more about CSV Files, refer to Wikipedia ; https://docs.python.org/2/library/csv.html

#1. Importing csv as DataFrame

dframe=pd.read_csv('demo.csv')
print (dframe) #CSV file has a proper header row
print()

#If the CSV file does not have a header, then the first row is automatically considered  the header
#This leads to data loss since any operations on the dataframe will not be reflected in the first row of data. In cases where we don't have a header, use the parameter header='false', within read_csv() function.

#2. Using readtable of pandas
#read_table() function can read more types of files than csv_read() since csv_read() can read only comma seperated data
#read_table() is more versatile since it has a parameter called seperator ,given as sep=' '. We can use any kind of seperator for reading data and mention it while reading.

#dframe2=pd.read_table('demo.csv',sep='!')
#print(dframe2)

#3. Reading pratial rows of a csv file

#Use the nrows parameter of read_csv to choose the rows for operations
print(pd.read_csv('demo.csv',nrows=2))

#4. Dumping data into a csv file

dframe.to_csv('outputCSV.csv',sep='!')
#The sep=' ' property of to_csv creates the csv files with the dataframe data values eperated by the seperator character mentioned by sep

#5. Selecting specific columns of a CSV file

dframe.to_csv('dataoutput.csv',columns=['Car','Revenue'])

#---------- NEXT LECTURE ----------#

#Handling Excel files in Python (Extension: .xlsx)
#Python by default cannot handle the following operations, hence new libraries are being installed: xlrd, openpyxl

excelfile=pd.ExcelFile('demo2.xlsx')
dframe=excelfile.parse('demo2')
print(dframe)
print()

#----------- NEXT LECTURE ----------#

#Handling HTML data - ew libraries: beautifulsoup4,html5lib,lxml ; lxml is not mentioned in the video lecture - info from https://stackoverflow.com/questions/34555135/pandas-read-html

#Extracting tables from HTML webpage (https://countrycode.org/)
url='https://countrycode.org/'
dflist=pd.io.html.read_html(url) #All the tables in the url variable are stored as list elements
dframe=dflist[0]
print(dframe)
print()

#Printing out the data row values without the header
print(dframe.values)
print()

#Printing out values of header columns
print(dframe.columns.values)











