import matplotlib.pyplot as plt
import collections
import seaborn as sns
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
from plotly import tools
from warnings import filterwarnings
bobData = pd.read_csv(f"C:\\Users\\hp\\OneDrive\\Desktop\\files\\deliveries.csv",low_memory=False)
matchData = pd.read_csv(f"C:\\Users\\hp\\OneDrive\\Desktop\\files\\matches.csv", low_memory=False)
umpiresList1 = list(matchData.umpire1.value_counts().index)
umpiresCount1 = list(matchData.umpire1.value_counts())
umpiresList2 = list(matchData.umpire2.value_counts().index)
umpiresCount2 = list(matchData.umpire2.value_counts())
umpires = {}
for name, match in zip(umpiresList1, umpiresCount1):
  umpires[name] = match 
for name, match in zip(umpiresList2, umpiresCount2):
  if name in umpires.keys():
    umpires[name] += match
  else:
    umpires[name] = match 
    sort_umpires = sorted(umpires.items(), key=lambda x: x[1], reverse=True)
names = []
matches = []
for value in sort_umpires:
  names.append(value[0])
  matches.append(value[1])
  fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.bar(range(10), matches[:10], color='lime')
plt.xlabel('Umpires', fontsize=20)
plt.ylabel('Matches', fontsize=20)
ax.set_xticks(range(10))
ax.set_xticklabels(names[:10], rotation=80, fontsize=20)
plt.show()