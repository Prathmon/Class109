import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

dice_res = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_res.append(dice1 + dice2)
   
mean = sum(dice_res)/len(dice_res)
median = statistics.median(dice_res)
mode = statistics.mode(dice_res)
standardDeviation = statistics.stdev(dice_res)

fig = ff.create_distplot([dice_res], ["Result"], show_hist = False)
fig.show()

print(mean)
print(mode)
print(median)
print(standardDeviation)