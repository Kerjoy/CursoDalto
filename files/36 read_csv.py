import csv
import pandas as pd

data_frame = pd.read_csv("files\\data_file.csv", names=["randomt1","randomt2","randomt3"]) #adding headers to csv files

#getting values of data of randomt1 row
tech1 = data_frame["randomt1"]

#sorting the data frame for randomt3
file_ascendent = data_frame.sort_values("randomt3")

#sorting the data frame descendent
file_descendent = data_frame.sort_values("randomt3", ascending=False)

#print(file_descendent)


data_frame_concat = pd.concat([file_ascendent,file_descendent]) #concat the data drames

first_row = data_frame.head(2) #aceesing to first 2 rows

last_row = data_frame.tail(2) #accesinf to last 2 rows

print(last_row)

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
