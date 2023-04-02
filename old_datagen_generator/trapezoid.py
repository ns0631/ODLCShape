def trapezoid(base, top, height, center_x, center_y, image_width, image_height):
    bottom_left = ( center_x - base / 2, center_y - height / 2 )
    bottom_right = ( center_x + base / 2, center_y - height / 2 )

    top_left = ( center_x - top / 2, center_y + height / 2 )
    top_right = ( center_x + top / 2, center_y + height / 2 )

    points = [ bottom_left, top_left, top_right, bottom_right ]

    return points
