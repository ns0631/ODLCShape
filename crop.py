import cv2, os, glob
import numpy as np

shapes = ["circle", "semicircle", "quarter_circle", "triangle", "square",
		  "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star",
		  "cross"]

paths = ['./dataset/test/', './dataset/train/', './dataset/valid/']
fpaths = list()
for path in paths:
    for shape in shapes:
        fpaths += glob.glob(path + shape + '/*.png') #+ glob.glob(path + '/*.jpg')
#breakpoint()
for fname in fpaths:
    #print(fname)
    os.system(f'backgroundremover -i {fname} -o {fname[:-4]}_modified.png')
    os.remove(fname)
