#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:10:35 2024

@author: blessingmkhonazi
"""

"""
remember that the first thing you need to do if you want to use pandas is to import them 
we learnt that we can create a file under the projects folder and name it pandas
then follow the following command to call it 
"""

import pandas as pd
#pd=pandas here
file = pd.read_csv("iris.csv")

"""
absolute path 
is as follows: /Users/blessingmkhonazi/css2024_day2_practice
-it gives the full location or path of the file

relative path
is as follows:iris.csv
-it gives the current location or directory, where you are running the file.

note that it is easier to use the relative path

data can also be accessed form the website and there is a command for it. check how to write a file from URL
"""

import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(df)

# sometime the data does not have header information for each columns, i.e no column names.
# you can add some in thsi way
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
print(df)
#after running this code we saw addtion of headers

"""
Reading different types of files

the commands change for different type of file, see the following

text file with a semi colon
df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

excel file
df = pd.read_excel("data_02/residentdoctors.xlsx")

json file
df = pd.read_json("data_02/student_data.json")


"""
df=pd.read_csv("Geospatial Data.txt",sep=";")
print(df)

df = pd.read_excel("residentdoctors.xlsx")
print(df)

df = pd.read_json("student_data.json")
print(df)

"""
ETL means extraction, transformation and loading
"""
"""
TRANSFORM

This is further manipulation of the data. 

columns can be removed in the follwoing manner:
"""

df=pd.read_csv("country_data_index.csv")

"""
pandas automatically adds an index column, which makes it redundant for the data that already has an index
so it can be removed in this manner
"""

df=pd.read_csv("country_data_index.csv", index_col=0)

"""
remember how to skip row lesson"""
df = pd.read_csv("country_data_index.csv",skiprows=5)
"""
print(df)
adding column names should also be learnt
"""

df = pd.read_csv("patient_data.csv")
print(df)

column_names = ["duration", "pulse", "max_pulse", "calories"]

df = pd.read_csv("patient_data.csv", header=None, names=column_names)
print (df)

"""
How to transform data and make it useful
"""

df = pd.read_excel("residentdoctors.xlsx")
print(df)

# Step 1: Extract the lower end of the age range (digits only)
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
print(df)
# \d+ means first decimal number and should be before the hyphen (-)


# Step 2: Convert the new column to float
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)
print(df)

df=pd.read_excel("residentdoctors.xlsx")
print(df)

#in this open data frame, some values are integers, floats, upper case mixed with lowe case
# consister is key, stick to one case
# age distribution column has combination of numbers and texts and it is invalid.
#marital status is also a mixture
#there is a READMEfile that explanes what all the numbers and vakues represent in the data shown

"""
# Extracting the lower age and using it as a category (this is to eliminate combination of texts and numbers)
"""
print(df.info())
# note that the data needs to be numbers, if text, rather define it outside
# everything needs to be numberical

"""
Working with dates
importing dates can be an issue if the format is not the same. 
best way is to save it as a flat format
"""
import pandas as pd
df=pd.read_csv("time_series_data.csv",index_col=0)
print(df)
print(df.info())

# # Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(pd)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
print(df)

# Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day




