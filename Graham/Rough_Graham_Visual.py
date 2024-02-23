import math
import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def subArrayCopy(arr, subArr, start, end):
    subArrayIndex = 0
    for i in range(start, end + 1):
        subArr[subArrayIndex] = arr[i]
        subArrayIndex += 1

def merge(arr, leftPointer, rightPointer):
    middleIndex = (rightPointer + leftPointer) // 2

    leftArray = [Point(0, 0)] * (middleIndex + 1 - leftPointer)
    rightArray = [Point(0, 0)] * (rightPointer - middleIndex)

    subArrayCopy(arr, leftArray, leftPointer, middleIndex)
    subArrayCopy(arr, rightArray, middleIndex + 1, rightPointer)

    leftArrayI = 0
    rightArrayI = 0
    arrPointer = leftPointer

    while leftArrayI < len(leftArray) and rightArrayI < len(rightArray):
        leftPoint = leftArray[leftArrayI]
        rightPoint = rightArray[rightArrayI]

        crossProduct = getCrossProduct(points[0], leftPoint, rightPoint)

        #for collinear points consider point futher away first
        #this is so later on we can reject any consecutive collinear points
        if crossProduct < 0 or (
                crossProduct == 0 and manhattanDistance(points[0], leftPoint) > manhattanDistance(points[0], rightPoint)):
            arr[arrPointer] = leftArray[leftArrayI]
            leftArrayI += 1

        else:
            arr[arrPointer] = rightArray[rightArrayI]
            rightArrayI += 1

        arrPointer += 1

    while leftArrayI < len(leftArray):
        arr[arrPointer] = leftArray[leftArrayI]
        leftArrayI += 1
        arrPointer += 1

    while rightArrayI < len(rightArray):
        arr[arrPointer] = rightArray[rightArrayI]
        rightArrayI += 1
        arrPointer += 1


def mergeSort(arr, leftPointer, rightPointer):
    if leftPointer < rightPointer:
        middleIndex = (rightPointer + leftPointer) // 2

        mergeSort(arr, leftPointer, middleIndex)
        mergeSort(arr, middleIndex + 1, rightPointer)

        merge(arr, leftPointer, rightPointer)

def generateRandomPoints(n):
    myPoints = []

    for i in range(n):
        myPoints.append(Point(random.randint(1, 100), random.randint(1, 100)))

    return myPoints


def getCrossProduct(p, q, r):
    crossProduct = (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)
    return crossProduct

def findBottomLeftMostPoint(points):
    minIndex = 0

    for i in range(1, len(points)):
        currentMin = points[minIndex]
        currentPoint = points[i]

        # Update to lowest point
        if currentPoint.y < currentMin.y:
            minIndex = i

        # If multiple points have same y coord, prioritise left most point
        elif currentPoint.y == currentMin.y:
            if currentPoint.x < currentMin.x:
                minIndex = i

    return minIndex

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

def getConvexHull(points):
    convexHull = []

    convexHull.append(points[0])
    convexHull.append(points[1])

    for i in range(2, len(points)):
        while len(convexHull) > 1 and getCrossProduct(convexHull[-2], convexHull[-1], points[i]) >= 0:
            convexHull.pop()
        convexHull.append(points[i])

    return convexHull


points = generateRandomPoints(500)
bottomLeftmostPoint = findBottomLeftMostPoint(points)

'''
 FOR BETTER SPACE COMPLEXITY COULD ALSO USE AN IN-PLACE ALGORITHM
'''
# Move origin to the start and sort the rest
points[bottomLeftmostPoint], points[0] = points[0], points[bottomLeftmostPoint]
mergeSort(points, 1, len(points) - 1)

'''
 COULD DO SWAPPING AND ETC ON MAIN 'POINTS' LIST INSTEAD OF CREATING SEPERATE LIST FOR CONVEX HULL:
 CREATE A TEMP INDEX VARIABLE AND MOVE THROUGH POINTS ARRAY.
'''
convexHull = getConvexHull(points)

# Plotting
scatterPlotPoints(points)
plotConvexHull(convexHull)
plt.show()