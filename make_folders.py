import os, glob
shapes = ["circle", "semicircle", "quartercircle", "triangle", "square", "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star", "cross"]

directories = ['train/', 'valid/', 'test/']

for dir in directories:
    label_path = './labels/' + dir
    img_path = './images/' + dir

    for shape in shapes:
        os.mkdir(img_path + shape)

    imgs = glob.glob(img_path + '*.png') + glob.glob(img_path + '*.jpg')
    labels = glob.glob(img_path + '*.txt')

    for img in imgs:
        label_file = img.replace('images', 'labels').replace('png', 'txt').replace('jpg', 'txt')
        #print(label_file)

        handle = open(label_file, 'r')
        first_line = handle.readline()
        handle.close()

        parsed_line = first_line.rstrip('\n').split(' ')
        correct_shape = shapes[ int(parsed_line[0]) ]

        final_path = img.replace(dir, dir + correct_shape + '/')
        print(final_path)

        os.rename(img, final_path)
