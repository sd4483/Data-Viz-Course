import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('data/2018WinterOlympics.csv')

trace1=go.Bar(x=df['NOC'],y=df['Gold'],name='Gold',marker=dict(color='#FFD700'))
trace2=go.Bar(x=df['NOC'],y=df['Silver'],name='Silver',marker=dict(color='#9EA0A1'))
trace3=go.Bar(x=df['NOC'],y=df['Bronze'],name='Bronnze',marker=dict(color='#CD7F32'))

#data=[go.Bar(x=df['NOC'],y=df['Total'])]

#data=[trace1,trace2,trace3]
medals = ['Gold','Silver', 'Bronze']
data = [go.Bar(x=df['NOC'],y=df[i],name=i) for i in medals]
#layout=go.Layout(title='Medals')
layout=go.Layout(title='Medals',barmode='stack')
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig)
