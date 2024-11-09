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
filterwarnings('ignore')
bobData = pd.read_csv(f"C:\\Users\\hp\\OneDrive\\Desktop\\files\\deliveries.csv",low_memory=False)
matchData = pd.read_csv(f"C:\\Users\\hp\\OneDrive\\Desktop\\files\\matches.csv", low_memory=False)
print(bobData.head())
print(matchData.head())
print((bobData.describe(include='all').T))
print(matchData.dtypes)
print(matchData.city.unique())
print(matchData.team1.unique())
print(matchData.team1.replace({'Rising Pune Supergiants':'Rising Pune Supergiant'}, regex=True, inplace=True))
print(matchData.team1.unique())
print(matchData.team2.unique())
print(matchData.toss_winner.unique())
print(matchData.winner.unique())
print(matchData.venue.unique())
print(matchData.venue.replace({'M Chinnaswamy Stadium' : 'M.Chinnaswamy Stadium', 'Punjab Cricket Association IS Bindra Stadium, Mohali' : 'Punjab Cricket Association Cricket Stadium, Mohali'},regex=True, inplace=True))
print(matchData.venue.isnull().sum())
print(matchData.city.isnull().sum())