import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    Size = []
    Time_spent = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Size.append(float(row["Size of TV"]))
            Time_spent.append(float(row["Average time spent"]))

    return {"x":Size, "y":Time_spent}
    
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Size of the TV vs Average Time Spent on TV: ", correlation[0,1])

def setup():
    data_path = "tv.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()