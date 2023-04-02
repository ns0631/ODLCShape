from math import *

def arc(center, measure, radius):
    points = list()

    if measure == 360:
        pass
    else:
        points.append(center)

    for degree in range(measure):
        x = center[0] + radius * cos(radians(degree))
        y = center[1] + radius * sin(radians(degree))

        points.append((x, y))

    return points
