import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter(x=df['horsepower'],y=df['mpg'],text=df['name'],mode='markers',
                                                    marker=dict(size=df['weight']/200,color=df['cylinders'],
                                                    showscale=True))]
layout = go.Layout(title='Bubble Chart',xaxis=dict(title='Horsepower'),
yaxis=dict(title='Miles per Gallon'))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
