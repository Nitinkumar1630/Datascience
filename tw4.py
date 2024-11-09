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
years = list(matchData.season.unique())
finalWinners = []
teams = []
winnersFrequency = []
for year in years:
  totalMatches = len(list(matchData[matchData.season==year]['winner']))
  finalWinners.append(list(matchData[matchData.season==year]['winner'])[totalMatches - 1])

winnersCollection = collections.Counter(finalWinners).most_common()

for (key, value) in winnersCollection:
  teams.append(key)
  winnersFrequency.append(value)
  fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.bar(range(len(teams)), winnersFrequency, color='maroon')

ax.set_xticks(range(len(teams)))
ax.set_xticklabels(teams, fontsize=15, rotation=40)
plt.xlabel('Teams', fontsize=20)
plt.ylabel('Number of Titles won by Teams', fontsize=25)
plt.show()