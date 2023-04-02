from math import *

# Alphanumeric list
texts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# color list
colors = ['white', 'black', 'gray', 'red', 'blue', 'green', 'yellow', 'purple', 'brown', 'orange']

# shape list
shapes = ["circle", "semicircle", "quarter_circle", "triangle", "square",
          "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star",
          "cross"]

side_number = {'triangle': 3,
               'square': 4,
               'pentagon': 5,
               'hexagon': 6,
               'heptagon': 7,
               'octagon': 8}

def rotate_point(point, angle, center, img_width, img_height):
    degrees = radians(angle)

    cartesian_x = point[0] - img_width / 2
    cartesian_y = img_height / 2 - point[1]

    cartesian_center_x = center[0] - img_width / 2
    cartesian_center_y = img_height / 2 - center[1]

    translated_x = cartesian_x - cartesian_center_x
    translated_y = cartesian_y - cartesian_center_y

    rotated_translated_x = translated_x * cos(degrees) - translated_y * sin(degrees)
    rotated_translated_y = translated_x * sin(degrees) + translated_y * cos(degrees)

    rotated_x = rotated_translated_x + cartesian_center_x
    rotated_y = rotated_translated_y + cartesian_center_y

    new_x = img_width / 2 + rotated_x
    new_y = img_height / 2 - rotated_y

    return (new_x, new_y)

def overlapping_area(l1, r1, l2, r2):
    x = 0
    y = 1

    # Area of 1st Rectangle
    area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])

    # Area of 2nd Rectangle
    area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])

    areaI = ((min(r1[x], r2[x]) -
              max(l1[x], l2[x])) *
             (min(r1[y], r2[y]) -
              max(l1[y], l2[y])))
    return (area1 + area2 - areaI)
