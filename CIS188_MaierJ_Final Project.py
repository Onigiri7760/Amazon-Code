#CIS188 Final Project
#Analzing Amazon Data
#Author: Jennifer Maier

#This program takes your amazon order history and displays what your
#total amount charged, average amount charged, medain total, maximum
#total, and minimum total is. It even puts the data into a bar graph so
#you can visually see how much you've spent on amazon daily.

import pandas as pd
from matplotlib import pyplot as plot

#Reads the file and stores it in table format
df = pd.read_csv('C:/Users/maier/Downloads/amazon-orders.csv')
#displays the information
print (df.head())

#Cleans up the file and gets rid of NaN values
df = df.fillna(0)
print (df.head())

#Makes sure the computer sees the numbers vs. characters
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

#Calculate Total Amounts
print ('Total Charged: ' + str(df["Total Charged"].sum()))

print ('Average Total Charged: ' + str( df["Total Charged"].mean()))

print ('Median Total Charged:  ' + str(df["Total Charged"].median()))

print ('Maximum Total Charged:  ' + str(df["Total Charged"].max()))

print ('Minumum Toatl Charged:  ' + str(df["Total Charged"].min()))

#helps recongize the data as dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

print (df.head())

#making the plot according to how much we spent in a day
daily_orders = df.groupby('Order Date').sum()["Total Charged"]
print (daily_orders.head())
print (daily_orders.plot.bar(figsize=(20,10)))
print (plot.show())

