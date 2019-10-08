import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Event_Records.csv')
activity_names = df['Activity'].unique()
accman_names = df['Account Manager'].unique()
