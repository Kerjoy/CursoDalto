import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv("graphical_problems\\file_boxplot.csv")

#making the line with data form csv
sns.boxplot(x="group",y="value",data = data_frame)

#show graphics
plt.show()

