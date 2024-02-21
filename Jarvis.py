import math
import random
import matplotlib.pyplot as plt

def generateRandomPoints(n):
    '''
    Returns a list of random coordinates between 0 - 100
            Parameters:
                    n (int): the number of points plotted

            Returns:
                    myPoints (list): a list of 2D points
    '''
    myPoints = []

    for i in range(n):
        myPoints.append([random.random() * 100, random.random() * 100])

    return myPoints

def calculateOrientation(p, q, r):
    crossProduct = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    # Clockwise
    if (crossProduct > 0):
        return 1
    # Counterclockwise
    elif (crossProduct < 0):
        return 2
    # Collinear
    else:
        return 0



def findLeftMostPoint(points):
    '''
    Returns the left most coordinate in the set of points given
            Parameters:
                    points (list): list of coordinates

            Returns:
                    leftMostIndex (int): the index of the left most coordinate
    '''
    leftMostIndex = 0

    for i in range(1, len(points)):
        currentLeftMost = points[leftMostIndex]
        currentPoint = points[i]

        # Update to new left most point
        if currentPoint[0] < currentLeftMost[0]:
            leftMostIndex = i

        # If multiple points have same x coord, prioritise largest y
        elif currentPoint[0] == currentLeftMost[0]:
            if currentPoint[1] > currentLeftMost[1]:
                leftMostIndex = i

    return leftMostIndex

def distance(p, q):
    return math.sqrt( math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2) )

def jarvismarch(points):
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
            orientation = calculateOrientation(points[p], points[r], points[q])
            if orientation == 1 or (
                    orientation == 0 and distance(points[p], points[r]) > distance(points[p], points[q])):
                q = r

        p = q
        if p == leftMostPoint:
            break

        outputSet.append(points[q])

    return outputSet

def scatterPlotPoints(points):
    xPoints = [point[0] for point in points]
    yPoints = [point[1] for point in points]

    for point in points:
        plt.scatter(point[0], point[1])


def plotConvexHull(points):
    xPoints = [point[0] for point in outputSet]
    yPoints = [point[1] for point in outputSet]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)

points = generateRandomPoints(15)
outputSet = jarvismarch(points)

scatterPlotPoints(points)
plotConvexHull(points)

plt.show()




