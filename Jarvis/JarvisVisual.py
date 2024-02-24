import math
import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generateRandomPoints(n):
    myPoints = []

    for i in range(n):
        myPoints.append(Point(random.randint(1, 100), random.randint(1, 100)))

    return myPoints

def getCrossProduct(p, q, r):
    crossProduct = (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)
    return crossProduct

def findLeftMostPoint(points):
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

def scatterPlotPoints(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    for point in points:
        plt.scatter(point.x, point.y)

def manhattanDistance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)

def plotConvexHull(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)

def jarvisMarch(points):
    '''
    Returns the list of points that lie on the convex outputSet (jarvis march algorithm)
            Parameters:
                    points (list): a list of 2D points

            Returns:
                    outputSet (list): a list of 2D points
    '''

    leftMostPoint = findLeftMostPoint(points)
    outputSet = []

    origin = points[leftMostPoint]
    outputSet.append(origin)

    p = leftMostPoint

    while (True):
        q = (p + 1) % len(points)
        for r in range(len(points)):
            if r == p:
                continue
            # find the greatest left turn
            # in case of collinearity, consider the farthest point
            crossProduct = getCrossProduct(points[p], points[r], points[q])
            if crossProduct > 0 or (
                    crossProduct == 0 and manhattanDistance(points[p], points[r]) > manhattanDistance(points[p], points[q])):
                q = r

        p = q
        if p == leftMostPoint:
            break

        outputSet.append(points[q])

    return outputSet

inputSet = generateRandomPoints(50)
outputSet = jarvisMarch(inputSet)

scatterPlotPoints(inputSet)
plotConvexHull(outputSet)

plt.show()