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

        crossProduct = getCrossProduct(arr[0], leftPoint, rightPoint)

        # for collinear points consider point futher away first
        # this is so later on we can reject any consecutive collinear points
        if crossProduct < 0 or (
                crossProduct == 0 and manhattanDistance(arr[0], leftPoint) > manhattanDistance(arr[0], rightPoint)):
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


def grahamScan(points):
    bottomLeftmostPoint = findBottomLeftMostPoint(points)

    points[bottomLeftmostPoint], points[0] = points[0], points[bottomLeftmostPoint]
    mergeSort(points, 1, len(points) - 1)

    convexHull = []

    convexHull.append(points[0])
    convexHull.append(points[1])

    for i in range(2, len(points)):
        while len(convexHull) > 1 and getCrossProduct(convexHull[-2], convexHull[-1], points[i]) >= 0:
            convexHull.pop()
        convexHull.append(points[i])

    return convexHull


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

def jarvisMarchModified(hulls):
    bottomLeftPoints = [hull[0] for hull in hulls]
    leftMostHullI = findLeftMostPoint(bottomLeftPoints)
    
    outputSet = [hulls[leftMostHullI][0]]
    currentHull = leftMostHullI
    currentPointI = 0
    p = hulls[leftMostHullI][0]
    q = hulls[leftMostHullI][1]
    
    while (True):
        q = hulls[currentHull][(currentPointI + 1) % len(hulls[currentHull])]
        
        for hullI in range(len(hulls)):
            for pointI in range(len(hulls[hullI])):
                r = hulls[hullI][pointI]
                
                crossProduct = getCrossProduct(p, r, q)
                if crossProduct > 0 or (
                crossProduct == 0 and manhattanDistance(p, r) > manhattanDistance(p, q)):
                    currentHull = hullI
                    currentPointI = pointI
                    q = hulls[hullI][pointI]
                    
        p = q
        if p == outputSet[0]:
            break

        outputSet.append(q)
    return outputSet

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
                    crossProduct == 0 and manhattanDistance(points[p], points[r]) > manhattanDistance(points[p],
                                                                                                      points[q])):
                q = r

        p = q
        if p == leftMostPoint:
            break

        outputSet.append(points[q])

    return outputSet


def createSubsets(points):
    t = 400
    subsets = []

    for i in range(0, len(points), t):
        subset = points[i: i + t]
        subsets.append(subset)

    return subsets


inputSet = generateRandomPoints(1600)
scatterPlotPoints(inputSet)

subsets = createSubsets(inputSet)
hulls = [grahamScan(subset) for subset in subsets]

outputSet = jarvisMarchModified(hulls)
plotConvexHull(outputSet)

plt.show()
