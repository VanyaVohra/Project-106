import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    Marks = []
    Days_present = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days_present.append(float(row["Days Present"]))

    return {"x":Marks, "y":Days_present}
    
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Marks vs Days Present: ", correlation[0,1])

def setup():
    data_path = "marks.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()