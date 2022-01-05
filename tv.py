import csv
import plotly.express as px

with open("tv.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Size of TV", y = "Average time spent")
    fig.show()
