import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv', index_col=0)

#data = [go.Bar(x=df.index, y=df[i], name=i) for i in df.columns]

data = [go.Bar(x=df[i], y=df.index, orientation='h', name=i) for i in df.columns]

layout = go.Layout(title='Mock Survey Results', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
