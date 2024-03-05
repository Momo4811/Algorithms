import math
import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
          return f"{self.x},{self.y}"

def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)

def cross_product(p,q,r):
    return (q.x - p.x)*(r.y - p.y) - (r.x - p.x)*(q.y - p.y)

def calculateOrientation(p, q, r):
        crossProduct = cross_product(p,q,r)

        
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
                        
        return leftMostIndex\

def jarvismarch(inputSet):      
    '''
    Returns the list of points that lie on the convex hull (jarvis march algorithm)
            Parameters:
                    inputSet (list): a list of 2D points

            Returns:
                    outputSet (list): a list of 2D points
    '''

    leftMostPoint = findLeftMostPoint(inputSet)
    outputSet = []
        
    origin = inputSet[leftMostPoint]
    outputSet.append(origin)
        
    p = leftMostPoint
        
    while True:
        q = (p + 1) % len(inputSet)
        for i in range(len(inputSet)):
                if i == p:
                        continue
                output = calculateOrientation(inputSet[p], inputSet[i], inputSet[q])
                if output == 0 and distance(inputSet[p], inputSet[i]) > distance(inputSet[p], inputSet[q]):
                        q = i
                        
                elif output == 2:
                        q = i
        p = q
        if p == leftMostPoint:
                break
                
        outputSet.append(inputSet[p])

    return outputSet




def generateRandomPoints(n):
    myPoints = []

    for i in range(n):
        myPoints.append(Point(random.randint(1, 1000), random.randint(1, 1000)))

    return myPoints

def plotConvexHull(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)

def scatterPlotPoints(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    for point in points:
        plt.scatter(point.x, point.y)


inputSet = generateRandomPoints(2000)
outputSet = jarvismarch(inputSet)
print(outputSet)
scatterPlotPoints(inputSet)
plotConvexHull(outputSet)

plt.show()