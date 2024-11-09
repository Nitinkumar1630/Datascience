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
wicketData = bobData[(bobData.player_dismissed != 'Not out') & (bobData.dismissal_kind != 'run out')]
bowlers = list(wicketData.bowler.value_counts().index)
wickets = list(wicketData.bowler.value_counts())
fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.plot(range(len(bowlers[:10])), wickets[:10], marker="o")
plt.xlabel('Top 10 bowlers', fontsize=20)
plt.ylabel('Wickets', fontsize=20)
ax.set_xticks(range(10))
ax.set_xticklabels(bowlers[:10], rotation=45, fontsize=15)
plt.show()