def cross(radius, center_x, center_y):
    distance = radius
    square_half = distance / 3

    leg_distance = 2 * square_half

    corner_1 = ( center_x - square_half, center_y + square_half )
    corner_2 = ( center_x + square_half, center_y + square_half )
    corner_3 = ( center_x + square_half, center_y - square_half )
    corner_4 = ( center_x - square_half, center_y - square_half )

    left_bottom = ( corner_4[0] - leg_distance, corner_4[1] )
    left_top = ( corner_4[0] - leg_distance, corner_1[1] )

    top_left = ( corner_1[0], corner_2[1] + leg_distance )
    top_right = ( corner_2[0], corner_2[1] + leg_distance )

    right_top = ( corner_3[0] + leg_distance, corner_2[1] )
    right_bottom = ( corner_3[0] + leg_distance, corner_3[1] )

    bottom_right = ( corner_3[0], corner_3[1] - leg_distance)
    bottom_left = ( corner_4[0], corner_3[1] - leg_distance)

    points = [ left_bottom, left_top, corner_1, top_left, top_right, corner_2,
    right_top, right_bottom, corner_3, bottom_right, bottom_left, corner_4 ]

    return points
