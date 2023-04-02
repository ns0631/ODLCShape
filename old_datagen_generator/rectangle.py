def rectangle(width, height, center_x, center_y, img_width, img_height):
    bottom_left = ( center_x -  width / 2, center_y - height / 2 )
    top_left = ( center_x -  width / 2, center_y + height / 2 )

    bottom_right = ( center_x +  width / 2, center_y - height / 2 )
    top_right = ( center_x + width / 2, center_y + height / 2 )

    points = [ bottom_left, top_left, top_right, bottom_right ]

    return points
