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
players = list(matchData.player_of_match.unique())
manOfMatchCount = matchData.player_of_match.value_counts()
fig = plt.figure(figsize=(12, 7))

ax = fig.add_subplot()
plt.barh(range(len(players[0:10])), manOfMatchCount[0:10], color='orange')

ax.set_yticks(range(10))
ax.set_yticklabels(list(matchData.player_of_match.unique())[0:10], fontsize=15)
for index, value in enumerate(manOfMatchCount[0:10]):
    plt.text(value, index, str(value))
plt.xlabel('Total count of Man of Matches', fontsize=20)
plt.ylabel('Palyers', fontsize=25)
plt.show()