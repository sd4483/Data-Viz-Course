import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

data = [go.Histogram(x=df['mpg'],xbins=dict(start=25,end=45,size=1))]
layout = go.Layout(title='No. of Cars Vs Miles Per Gallon')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
