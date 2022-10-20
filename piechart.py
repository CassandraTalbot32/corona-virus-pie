import pandas as pd
from matplotlib.pyplot import pie, axis, show
%matplotlib inline

# Read file 
df = pd.read_csv ('chart_work.csv')

# Calculate percentages to use in pie chart
sums = df.groupby(df["Product Name;"])["Number Of Bugs"].sum()
axis('equal');
pie(sums, labels=sums.index);
show()
