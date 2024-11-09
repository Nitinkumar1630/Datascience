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
dateSplit = matchData['date'].str.split("-")
matchData['season'] = dateSplit.str.get(0)
match_per_season = matchData.groupby(['season'])['id'].count().reset_index().rename(columns={'id' : 'matches'})
match_per_season.style.background_gradient(cmap='PuBu')
print(match_per_season)
plt.figure(figsize=(12, 7))
sns.countplot(x=matchData.season)
plt.xlabel('Years', fontsize=15)
plt.ylabel('Total Matches', fontsize=15)
plt.show()