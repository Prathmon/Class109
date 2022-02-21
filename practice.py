import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics

file1 = pd.read_csv("height-weight.csv")

height_list = file1["Height(Inches)"].to_list()
weight_list = file1["Weight(Pounds)"].to_list()

heightMean = statistics.mean(height_list)
weightMean = statistics.mean(weight_list)
heightMedian = statistics.median(height_list)
weightMedian = statistics.median(weight_list)
heightMode = statistics.mode(height_list)
weightMode = statistics.mode(weight_list)
heightStanDev = statistics.stdev(height_list)
weightStanDev = statistics.stdev(weight_list)

print(heightMean)
print(weightMean)
print(heightMedian)
print(weightMedian)
print(heightMode)
print(weightMode)
print(heightStanDev)
print(weightStanDev)