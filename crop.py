import cv2, os, glob
import numpy as np

#fname = './2865.png'
#path = './backgroundremoval_tool/'
paths = ['./dataset/images/test/', './dataset/images/train/', './dataset/images/valid/']
fpaths = list()
for path in paths:
    fpaths += glob.glob(path + '*.png') + glob.glob(path + '*.jpg')
#breakpoint()
for fname in fpaths:
    #print(fname)
    os.system(f'backgroundremover -i {fname} -o {fname[:-4]}_modified.png')
    os.remove(fname)
    #cv2.waitKey(0)
    #cv2.imwrite(fname[:-4] + '_cropped.png', cropped_img)
