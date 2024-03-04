import matplotlib.pyplot as plt

def scatterPlotPoints(points):
    xPoints = [point[0] for point in points]
    yPoints = [point[1] for point in points]

    for point in points:
        plt.scatter(point[0], point[1])

def plotConvexHull(points):
    xPoints = [point[0] for point in points]
    yPoints = [point[1] for point in points]

    xPoints.append(xPoints[0])
    yPoints.append(yPoints[0])

    plt.plot(xPoints, yPoints)