import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv("graphical_problems\\file_bar.csv")

#making the line with data form csv
sns.barplot(x="source",y="income",data = data_frame)

#this method sum all values on field given
total_income = data_frame["income"].sum()

#showing total_income
print(f"Total income{total_income}")

#show graphics
plt.show()

