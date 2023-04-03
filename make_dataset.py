import os

path = './dataset/'

folders = ['train/', 'valid/', 'test/']
shapes = ["circle", "semicircle", "quarter_circle", "triangle", "square", "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star", "cross"]
#sub_directories = ['images/', 'labels/']

for folder in folders:
    os.mkdir(path + folder)
    for shape in shapes:
        os.mkdir(path + folder + shape)
