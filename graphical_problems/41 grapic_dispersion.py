import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv("graphical_problems\\file_bar.csv")

#making the line with data form csv
sns.scatterplot(x="source",y="income",data = data_frame)

#show graphics
plt.show()

