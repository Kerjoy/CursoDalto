import csv
import pandas as pd

data_frame = pd.read_csv("files\\data_file.csv", names=["randomt1","randomt2","randomt3","randomt4"]) #adding headers to csv files

#getting values of data of randomt1 row
tech1 = data_frame["randomt1"]

#sorting the data frame for randomt3
file_ascendent = data_frame.sort_values("randomt3")

#sorting the data frame descendent
file_descendent = data_frame.sort_values("randomt3", ascending=False)

#print(file_descendent)


data_frame_concat = pd.concat([file_ascendent,file_descendent]) #concat the data drames

first_row = data_frame.head(0) #aceesing to first 2 rows

last_row = data_frame.tail(2) #accesing to last 2 rows

print(first_row)

#retrieve number of rows and columns, retun a tuple (0,1)

rows_and_columns_shape = data_frame.shape
rows,columns = data_frame.shape

print(rows,columns)

#retrieving stadistical dato from dataframe
data_frame_stadistical = data_frame.describe()
print(data_frame_stadistical)

#accesing to specific element from data frame with loc
specific_element = data_frame.loc[2,"randomt3"]

#accesing to specific element from data frame with iloc
specific_element_with_iloc = data_frame.iloc[2,2]

print(specific_element_with_iloc)

#accesing all rows in a column
second_column = data_frame.loc[:,"randomt3"]
#works same way
second_column = data_frame.iloc[:,2]
print(second_column)

#accesing to row with number greater than 3
greater = data_frame.loc[data_frame["randomt4"]>2,:]

print(greater)

#getting values of column tech1
#t1 = data_frame["Tech1"]
#print(t1)


#the limited way built in python
"""
with open("files\\data_file.csv") as csv_data:
    reader = csv.reader(csv_data)
    for row in reader:
        print(row)
"""
