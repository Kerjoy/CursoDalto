import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("graphical_problems\\file_lineal.csv")

#making the line with data form csv
sns.lineplot(x="date",y="line",data = data_frame)

#creating a dot for the highest value, i can make this dinamic if i calculate the higest value
plt.plot("10-01",20,"o")

#show graphics
plt.show()