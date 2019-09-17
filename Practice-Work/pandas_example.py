import pandas as pd

df = pd.read_csv('salaries.csv')
#print(df)
#print(df['Salary'])
#print(df[['Name','Salary']]) """--> Need to add another set of paranthesis for printing values from multiple columns"""
#print(df['Salary'].min())
#print(df['Salary'].mean()) """--> Prints only boolean statements such as True or False"""
#print(df[df['Age']>30]) """--> Prints the actual values if there are any that satisfy the condition"""

#print(df['Age'].unique()) """--> Prints all the unique values in the columns (non-repeated values)"""
#print(df['Age'].nunique()) """--> Prints how many unique values are there in the column"""

#print(df.columns) """--> Prints all the column names"""
#print(df.info()) """--> Prints all the info about the dataframe, like data types, num of columns, etc"""
#print(df.describe()) """--> Prints the count, min, max, mean, std for all the numerical columns in the df"""
