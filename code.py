import csv
import pandas as pd
import ploty.graph_objects as go


df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.figure(go.Scatter(
    x = df.groupby("level1"["attempt"].mean(),
    y = ['level 1','level 2','level 3','level 4'],
    orientation = 'h'))

fig.show()