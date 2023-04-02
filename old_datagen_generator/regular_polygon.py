from math import *

def regular_polygon(side_number, radius, center_x, center_y):
    points = list()

    unit_angle = 360 / side_number
    for side in range(side_number):
        angle_measure = unit_angle * side
        x = radius * cos(radians(angle_measure)) + center_x
        y = radius * sin(radians(angle_measure)) + center_y
        points.append((x, y))

    return points
