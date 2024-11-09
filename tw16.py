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
season_data=matchData[['id','season']].merge(bobData, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
season = season_data.groupby(['season'])['total_runs'].sum().reset_index().set_index('season')
fig = px.line(season, x=season.index, y="total_runs", labels=dict(x="Season", y="Total Runs"))
fig.update_layout(title="Total Runs Across the Seasons ",
                  titlefont={'size': 26},template='simple_white')
fig.show()
