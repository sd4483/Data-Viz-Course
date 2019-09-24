#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('data/iris.csv')

# Define the traces
setosa = df[df['class']=='Iris-setosa']['petal_length']
versicolor = df[df['class']=='Iris-versicolor']['petal_length']
virginica = df[df['class']=='Iris-virginica']['petal_length']
# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-setosa']['petal_length']


# Define a data variable
hist_data = [setosa,versicolor,virginica]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.2,0.2,0.2])
pyo.plot(fig)
