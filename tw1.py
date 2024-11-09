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
teams = list(matchData.toss_winner.value_counts().index)
toss_winners = list(matchData.toss_winner.value_counts())
match_winners = list(matchData.winner.value_counts())
print(match_winners.pop(len(match_winners)-1))
fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()

n = 1
t = 2
d = len(teams)
w = 0.8
x_values1 = [t*element + w*n for element in range(d)] 


n = 2
t = 2
d = len(teams)
w = 0.8
x_values2 = [t*element + w*n for element in range(d)] 

ax.set_yticks(x_values1)
ax.set_yticklabels(teams)
plt.barh(x_values1, toss_winners)
plt.barh(x_values2, match_winners)
plt.show()