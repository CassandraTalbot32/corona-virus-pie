import pandas as pd
from matplotlib.pyplot import pie, axis, show
%matplotlib inline

df = pd.read_csv ('chart_work.csv')

sums = df.groupby(df["Product Name;"])["Number Of Bugs"].sum()
axis('equal');
pie(sums, labels=sums.index);
show()
