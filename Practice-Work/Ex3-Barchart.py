#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df=pd.read_csv('data/mocksurvey.csv')
#index=df.columns.values
#index[0]='Questions'
#df=df.set_index('Questions')
df=df.set_index(df.columns.values[0])
# create traces using a list comprehension:
trace0=go.Bar(x=df.index,y=df['Strongly Agree'],name='Strongly Agree')
trace1=go.Bar(x=df.index,y=df['Somewhat Agree'],name='Somewhat Agree')
trace2=go.Bar(x=df.index,y=df['Neutral'],name='Neutral')
trace3=go.Bar(x=df.index,y=df['Somewhat Disagree'],name='Somewhat Disagree')
trace4=go.Bar(x=df.index,y=df['Strongly Disagree'],name='Strongly Disagree')

#trace5=go.Bar(x=df['Strongly Agree'],y=df.index,name='Strongly Agree')
#trace6=go.Bar(x=df['Somewhat Agree'],y=df.index,name='Somewhat Agree')
#trace7=go.Bar(x=df['Neutral'],y=df.index,name='Neutral')
#trace8=go.Bar(x=df['Somewhat Disagree'],y=df.index,name='Somewhat Disagree')
#trace9=go.Bar(x=df['Strongly Disagree'],y=df.index,name='Strongly Disagree')

data1=[trace0,trace1,trace2,trace3,trace4]
#data2=[trace5,trace6,trace7,trace8,trace9]

# create a layout, remember to set the barmode here
layout=go.Layout(title='Mock Survey Results',barmode='stack')

# create a fig from data & layout, and plot the fig.
fig1=go.Figure(data=data1,layout=layout)
#fig2=go.Figure(data=data2,layout=layout)

pyo.plot(fig1)
#pyo.plot(fig2)
