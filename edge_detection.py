import cv2, os, glob
import numpy as np

def floodfill(image, startx, starty):
    global grid

    area = 0
    height, width = image.shape[:2]
    grid[starty][startx] = 255
    #print(grid.shape)
    stack = [ (startx, starty) ]
    while len(stack) > 0:
        x, y = stack[-1]
        del stack[-1]

        grid[y][x] = 255
        area += 1

        if x + 1 < width and grid[y][x + 1] == 0 and sum(image[y, x + 1, :]) < 10:
            stack.append( (x + 1, y) )
        if x > 0 and grid[y][x - 1] == 0 and sum(image[y, x - 1, :]) == 0:
            stack.append( (x - 1, y) )
        if y + 1 < height and grid[y + 1][x] == 0 and sum(image[y + 1, x, :]) < 10:
            stack.append( (x, y + 1) )
        if y > 0 and grid[y - 1][x] == 0 and sum(image[y - 1, x, :]) < 10:
            stack.append( (x, y - 1) )


    return area

#paths = ['./dataset/images/test/', './dataset/images/train/', './dataset/images/valid/']
paths = ['./finished_shapes_2/']#['./darkened_shapes/']
fpaths = list()
for path in paths:
    fpaths += glob.glob(path + '*.png') + glob.glob(path + '*.jpg')
#breakpoint()
for fpath in fpaths:
    img = cv2.imread(fpath)
    #fname = './backgroundremoval_tool/IMG_1522.png'
    #img = cv2.imread(fname)
    height = np.shape(img)[0]
    width = np.shape(img)[1]
    grid = np.zeros(img.size // 3 ).reshape((img.shape[0], img.shape[1]))

    #new_height, new_width = cropped_img.shape
    #Remove black at 4 corners
    r1 = floodfill(img, 0, 0)
    r2 = floodfill(img, 0, height - 1)
    r3 = floodfill(img, width - 1, 0)
    r4 = floodfill(img, width - 1, height - 1)

    bgr_img = cv2.cvtColor(np.float32(grid), cv2.COLOR_GRAY2BGR)
    #breakpoint()
    #cv2.imwrite(fpath[:fpath.find('_')] + fpath[-4:], bgr_img)
    cv2.imwrite(fpath[:-4] + '_modified.png', bgr_img)
    print(fpath[:-4] + '_modified.png')
    #os.remove(fpath)
