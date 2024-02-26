import matplotlib.pyplot as plt

def scatterPlotPoints(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    for point in points:
        plt.scatter(point.x, point.y)

def plotConvexHull(points):
    xPoints = [point.x for point in points]
    yPoints = [point.y for point in points]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)