import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


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

    
    #always pops on first two points
    convexHull = []
    convexHull.append(points[0])
    convexHull.append(points[1])

    
    #instead of pushing on point[i], we check its orientation first
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


def binary_search(hull, p):
    left, right = 0, len(hull) - 1
    while abs(right - left) > 1:
        mid = (left + right) // 2
        crossProduct = getCrossProduct(p, hull[left], hull[mid])
        if crossProduct < 0  or (
            crossProduct == 0 and manhattanDistance(p, hull[mid]) > manhattanDistance(p, hull[left])):
            left = mid 
        else:
            right = mid
            
    return right if getCrossProduct(p, hull[left], hull[right]) < 0 else left

def jarvisMarchModified(hulls, m):
    bottomLeftPoints = [hull[0] for hull in hulls]
    leftMostHullI = findLeftMostPoint(bottomLeftPoints)

    outputSet = [hulls[leftMostHullI][0]]
    currentHull = leftMostHullI
    currentPointI = 0
    p = hulls[leftMostHullI][0]

    while len(outputSet) < m:
        q = hulls[currentHull][(currentPointI + 1) % len(hulls[currentHull])]

        for hullI in range(len(hulls)):
            pointI = binary_search(hulls[hullI], p)
            r = hulls[hullI][pointI]

            crossProduct = getCrossProduct(p, q, r)
            if crossProduct < 0  or (
                    crossProduct == 0 and manhattanDistance(p, r) > manhattanDistance(p, q)):
                currentHull = hullI
                currentPointI = pointI
                q = hulls[hullI][pointI]

        p = q
        if p == outputSet[0]:
            return outputSet

        outputSet.append(p)

    # in case of failure
    return []

def createSubsets(inputSet, m):
    subsets = []
    for i in range(0, len(inputSet), m):
        subset = inputSet[i: i + m]
        if len(subset) < 3:
            return []
        subsets.append(subset)

    return subsets


def chansScan(inputSet):
    t = 0
    outputSet = []

    while not outputSet:
        t += 1
        m = 2 ** 2 ** t

        subsets = createSubsets(inputSet, m)

        #invalid number of subsets, move onto next m
        if not subsets:
            continue
        
        hulls = [grahamScan(subset) for subset in subsets]
        outputSet = jarvisMarchModified(hulls, m)

        #print(m)

    return outputSet
