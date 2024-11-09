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
fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot()
plt.bar(range(2), list(matchData.toss_decision.value_counts()), color='red')
plt.xlabel('Decision', fontsize=20)
plt.ylabel('Matches', fontsize=20)
ax.set_xticks(range(2))
ax.set_xticklabels(list(matchData.toss_decision.value_counts().index), rotation=80, fontsize=20)
plt.show()