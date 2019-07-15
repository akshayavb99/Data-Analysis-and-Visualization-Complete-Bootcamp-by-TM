#Assignment 2 under TakenMind Analytics Internship - Dated July 15,2019

import numpy as np
import pandas as pd

#QUESTION:
#   1. Create a single .xlsx file with 10 sheets inside filled with dummy data.
#   2. Read the .xlsx file using pandas
#   3. Export every single sheet of the .xlsx file as a .csv file. (The Output should produce 10 .csv files that contains values of each sheet of .xlsx file respectively)

#Reading from Excel Workbook
xlsfile=pd.ExcelFile('Assignment2_ExcelData.xlsx') #The function ExecelFile() reads the workbook as whole and not individual sheets
#df1=pd.read_excel(excelfile,'Sheet1') #To read an individual sheet we can use the parse() function or read_excel() function
df=list()
sheet_name=xlsfile.sheet_names #the property sheet_names can be used to store all the names of the sheets in the parsed workbook.
for name in sheet_name:
    df.append(pd.read_excel(xlsfile,name)) #Each element of the list df is the data of a particular sheet
print(df[3])

#Exporting to 10 .csv files
sheet_num=1
for i in df:
    i.to_csv('sheet'+str(sheet_num)+'-converted.csv')
    sheet_num+=1

