import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))

    return {"x":Coffee, "y":Sleep}
    
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Coffee drunk vs Sleep in hours: ", correlation[0,1])

def setup():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()