import matplotlib.pyplot as plt
import math
import random

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
          return f"({self.x},{self.y})"

def worst_case_points(n):

        # h = n for worst case
        # non collinear points, hence points are on the convex hull
        # in the form of a circle
        mult = 100000
        inputSet = set()
        i=1
        while True:
            inputSet.add(Point(int(math.cos(2*math.pi*i/n)*mult), int(math.sin(2*math.pi*i/n)*mult)))
            i+=1
            if len(inputSet) == n:
                break
        return list(inputSet)


def scatterPlotPoints(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    for point in points:
        plt.scatter(point.x, point.y)

inputSet = worst_case_points(100000)
print(inputSet)
scatterPlotPoints(inputSet)
plt.show()