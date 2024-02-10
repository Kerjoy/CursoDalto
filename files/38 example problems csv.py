import pandas as pd

data_frame = pd.read_csv("files\\data_example.csv")

#change type of data on column

data_frame['Age'] = data_frame['Age'].astype(str)

print(type(data_frame['Age'][0]))

#replacing data in data frame

data_frame['Name'].replace("Juan","Ker",inplace=True)

#print(data_frame['Name'])

#delete the rows with empty cells
data_frame = data_frame.dropna()

#delete duplicate rows

data_frame = data_frame.drop_duplicates()

print(data_frame)

#creating a CSV with result data_frame(processed)
data_frame.to_csv("files\\data_example_processed.csv")