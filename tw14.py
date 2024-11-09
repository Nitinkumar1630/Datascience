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
fieldersData = bobData[(bobData.player_dismissed != 'Not out') & 
                   (bobData.dismissal_kind != 'bowled') & (bobData.dismissal_kind != 'retired hurt') & (bobData.dismissal_kind != 'hit wicket')
                    & (bobData.dismissal_kind != 'obstructing the field') & (bobData.dismissal_kind != 'lbw') & (bobData.fielder != 'No fielder')]
fieldersName = list(fieldersData.fielder.value_counts().index)
fieldingCount = list(fieldersData.fielder.value_counts())
fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.bar(range(len(fieldersName[:10])), fieldingCount[:10], color='cyan')
plt.xlabel('Top 10 fielders', fontsize=20)
plt.ylabel('Fielding Count', fontsize=20)
ax.set_xticks(range(len(fieldersName[:10])))
ax.set_xticklabels((fieldersName[0:10]), rotation=45, fontsize=10)
plt.show()