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
wicketDecision = bobData[(bobData.player_dismissed != 'Not out')]
dismisselType = list(wicketDecision.dismissal_kind.value_counts().index)
dismisselCount = list(wicketDecision.dismissal_kind.value_counts())
fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.bar(range(len(dismisselType)), dismisselCount, color='red')
plt.xlabel('Dismissel Type', fontsize=20)
plt.ylabel('Dismissel Count', fontsize=20)
ax.set_xticks(range(len(dismisselType)))
ax.set_xticklabels((dismisselType), rotation=45, fontsize=10)
plt.show()