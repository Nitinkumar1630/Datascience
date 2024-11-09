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
topCitiesCount = list(matchData.city.value_counts()[0:10])
topCities = list(matchData.city.value_counts()[0:10].index)
normalizedCount = []
totalMatchesPlayed = sum(topCitiesCount)
normalizedCount = [ (matches/totalMatchesPlayed)*100 for matches in topCitiesCount]
plt.figure(figsize=(12,9))
plt.pie(normalizedCount, autopct="%0.1f%%")
plt.legend(topCities, loc="upper left")
plt.show()
