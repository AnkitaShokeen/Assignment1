#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd
import numpy as np
context = {
    'Name':['Ankita','Ajay','Sakshi'],
    'Age' :[21,23,21],
    'Email_id':['anki@gmail.com','ajay@gmail.com','saks@gmail.com'],
    'Phone_no' :[8368750600,9971000135,8588033135]
     }
print("Your Dataframe is as follows: ")
df = pd.DataFrame(context)
print(df)


#Q.2 - Download the dataset from this link , 

#Import the data and print the following :
#a.) First 5 rows of Dataframe 
#b.) First 10 rows of the Dataframe 
#c.) find basic statistics on the particular dataset. 
#d.) Find the last 5 rows of the dataframe 
#e.) Extract the 2nd column and find basic statistics on it.

import pandas as pd
import numpy as np

file = pd.read_csv("weather.csv")

print("The first five rows of the dataframe are:")
print (file.head())

print("The first ten rows of the dataframe are:")
print (file.head(10))

print("Basic statistics of the dataframe are:")
print(file.describe(include='all'))

print("The last five rows of the dataframe are:")
print (file.tail())

print("Basic statistics of 2nd column is:")
print(file.describe(include='all').Location)
