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
resultMargins = []
for year in years:
  seasonData = matchData[matchData.season == year]
  resultMargins.append(list(seasonData.result_margin))
  fig = plt.figure(figsize=(12, 12))

ax = fig.add_subplot()
plt.xlabel('Season', fontsize=20)
plt.ylabel('Result margin', fontsize=20)

for xe, ye in zip(years, resultMargins):
    plt.scatter([xe] * len(ye), ye)

ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.show()