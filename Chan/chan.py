def chansAlgorithm(points):
    t = 1
    while True:
        h = min(len(points), t)
        subsets = [points[i:i + h] for i in range(0, len(points), h)]
        hulls = [grahamHull(subset) for subset in subsets]
        hull = jarvisHull(hulls)
        if len(hull) <= t:
            return hull
        t *= 2