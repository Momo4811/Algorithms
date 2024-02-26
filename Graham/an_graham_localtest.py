import random
from point import Point
import matplotlib.pyplot as plt
from an_graham_visuals import scatterPlotPoints, plotConvexHull
from an_grahamscan import *

print("Graham Scan")
listofpoints = [Point(random.randint(0,100000),random.randint(0,100000)) for i in range(500)]
hullpoints = akn_graham_scan(listofpoints)
print(hullpoints)

scatterPlotPoints(listofpoints)
plotConvexHull(hullpoints)
plt.show()