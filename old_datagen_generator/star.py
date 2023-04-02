from math import *

def star(radius, center_x, center_y):
    distance = radius
    degree_unit = 36
    points = list()

    for tooth in range(10):
        radian_measure = radians(degree_unit * tooth)
        if tooth % 2 == 0:
            x = center_x + distance * cos(radian_measure)
            y = center_y + distance * sin(radian_measure)
        else:
            x = center_x + distance * cos(radian_measure) / 2
            y = center_y + distance * sin(radian_measure) / 2
        points.append( (x, y) )
    return points
