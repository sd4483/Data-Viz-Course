import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from collections import Counter

df = pd.read_csv('Event_Records.csv')
activity_names = df['Activity'].unique()
accman_names = df['Account Manager'].unique()
accman_real = ['Lei','Kalebh','Isha','Jayden']

df2 = df[['Activity','Account Manager']][:204]
df2.set_index('Account Manager', inplace=True)

df_lei = df2.loc['Lei']
freq_lei = Counter(df_lei['Activity'])

print(freq_lei)
print(activity_names)
"""
for i in activity_names:
    if i == freq_lei.keys():
        print (freq_lei[i])
"""
fig = go.Figure(data = [go.Table(header=dict(values=['Activity','Lei']),
                cells=dict(values=[[activity_names],[freq_lei[activity_names]]]))])
fig.show()
