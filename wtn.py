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

plt.figure(figsize=(12,7))
sns.countplot(y=matchData.winner, order=matchData.winner.value_counts().index)
plt.xlabel('Total Matches won by Teams', fontsize=15)
plt.ylabel('Teams', fontsize=15)
plt.show()