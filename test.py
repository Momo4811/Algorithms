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
        
        inputSet = set()
        i=0
        mult = 2**(n) if n < 20 else 1000000
        while True:
            inputSet.add(Point(int(math.cos(2*math.pi*i/n)*mult), int(math.sin(2*math.pi*i/n)*mult)))
            if len(inputSet) == n:
                break
            i+=1
        return list(inputSet)
# Reusable data structures and functions for the algorithms
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
          return f"({self.x},{self.y})"

def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)

def cross_product(p,q,r):
    return (q.x - p.x)*(r.y - p.y) - (r.x - p.x)*(q.y - p.y)


# Auxilliary functions for Jarvis March
def calculate_orientation(p, q, r):
        crossProduct = cross_product(p,q,r)

        if (crossProduct > 0): return 1         # Clockwise
        elif (crossProduct < 0): return 2       # Counterclockwise
        else: return 0                          # Collinear
        
def find_left_most_point(points):
        leftMostIndex = 0
        for i in range(1, len(points)):
                currentLeftMost = points[leftMostIndex]
                currentPoint = points[i]
                
                # Update to new left most point
                if currentPoint.x < currentLeftMost.x:
                        leftMostIndex = i
                
                # If multiple points have same x coord, prioritise largest y
                elif currentPoint.x == currentLeftMost.x:
                        if currentPoint.y > currentLeftMost.y:
                                leftMostIndex = i
                        
        return leftMostIndex

def jarvismarch(inputSet):      
    leftMostPoint = find_left_most_point(inputSet)
    outputSet = []
        
    origin = inputSet[leftMostPoint]
    outputSet.append(origin)
        
    p = leftMostPoint
        
    while True:
        q = (p + 1) % len(inputSet)
        for i in range(len(inputSet)):
                if i == p:
                        continue
                output = calculate_orientation(inputSet[p], inputSet[i], inputSet[q])
                if output == 0 and distance(inputSet[p], inputSet[i]) > distance(inputSet[p], inputSet[q]):
                        q = i
                        
                elif output == 2:
                        q = i
        p = q
        if p == leftMostPoint:
                break
                
        outputSet.append(inputSet[p])

    return outputSet



def scatterPlotPoints(points):
    for point in points:
        plt.scatter(point.x, point.y)

def plotConvexHull(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)

inputSet = worst_case_points(1000000)
print(inputSet)
# scatterPlotPoints(inputSet)
# plt.show()