import os, cv2, random, sys, imutils
import numpy as np

shapes = ["circle", "semicircle", "quarter_circle", "triangle", "square",
		  "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star",
		  "cross"]

path = './finished_shapes_2/'
#path = './chars/'
folder = os.listdir(path)

def colorify(img, scale):
	height, width, dim = img.shape
	#scale = 3
	new_width = width // scale
	new_height = height // scale
	img = cv2.resize(img, (new_width, new_height))

	grid = np.zeros(3 * new_width * new_height).reshape((new_height, new_width, 3))

	radius = 5
	base_color = np.random.randint(low=2 * radius, high=255 - radius, size=(3,))
	grid += base_color

	noise = np.random.randint(low=-radius, high=radius, size=grid.size).reshape((new_height, new_width, 3))
	grid += noise
	grid = np.uint8(grid)

	colored = np.where(img != [0,0,0])
	miny = max(0, np.min(colored[0]) - 5)
	maxy = min(new_height - 1, np.max(colored[0]) + 5)
	minx = max(0, np.min(colored[1]) - 5)
	maxx = min(new_width - 1, np.max(colored[1]) + 5)
	#breakpoint()
	img = img[miny : maxy, minx : maxx, :]
	#print(img.shape)
	colored = np.where(img != [0,0,0])
	#colored = np.where(img == [240,240,240])
	#breakpoint()
	for i, py in enumerate(colored[0]):
		px = colored[1][i]
		img[py, px, :] = grid[py, px, :]

	#breakpoint()
	return img

def superimpose(image_1, image_2, scale_1, scale_2):
	image_2 = colorify(image_2, scale_2)
	image_1 = colorify(image_1, scale_1)

	shape_height, shape_width, shape_dim = image_2.shape
	letter_height, letter_width, letter_dim = image_1.shape

	centerx = shape_width // 2
	centery = shape_height // 2
	startx = centerx - letter_width // 2
	starty = centery - letter_height // 2

	colored_char = np.where(image_1 != [0,0,0])
	for i, py in enumerate(colored_char[0]):
		px = colored_char[1][i]
		image_2[py + starty, px + startx, :] = image_1[py, px, :]

	return image_2

def paste(background, object, centerx, centery):
	base_height, base_width, base_dim = background.shape
	shape_height, shape_width, shape_dim = object.shape

	#centerx = shape_width // 2
	#centery = shape_height // 2
	startx = centerx - shape_width // 2
	starty = centery - shape_height // 2

	colored = np.where(object != [0,0,0])
	for i, py in enumerate(colored[0]):
		px = colored[1][i]
		background[py + starty, px + startx, :] = object[py, px, :]
	return background

background_dir = './backgrounds/'
background_files = os.listdir(background_dir)

for i in range(int(sys.argv[1])):
	print(f'{i} of {sys.argv[1]}')

	fpath = background_dir + random.choice(background_files)
	#print(fpath)
	background_img = cv2.imread(fpath)
	background_height, background_width, background_dims = background_img.shape

	shape_path = './finished_shapes_2/'
	shape_files = os.listdir(shape_path)
	letter_path = './chars/'
	letter_files = os.listdir(letter_path)
	shape_f = random.choice(shape_files)
	letter_f = random.choice(letter_files)

	shape_name = shape_f[:shape_f.find('_')]
	if shape_name == 'semicircle':
		shape_name = 'semi_circle'
	#breakpoint()

	#print(shape_f, letter_f)
	tilt = random.randint(0, 359)
	shapeimg1 = imutils.rotate_bound(cv2.imread(shape_path + shape_f), tilt)
	letterimg1 = imutils.rotate_bound(cv2.imread(letter_path + letter_f), tilt)
	final = superimpose(letterimg1, shapeimg1, 2, 2)

	height, width, dim = final.shape
	height = height // 3
	width = width // 3

	final = cv2.resize(final, (width, height))

	centerx = random.randint(100, background_width - 100)
	centery = random.randint(100, background_height - 100)
	#print(centerx, centery)
	background_img = paste(background_img, final, centerx, centery)

	max_dim = int(1.5 * max(height, width))
	starty = int(centery - 0.75 * height)
	startx = int(centerx - 0.75 * width)
	background_img = cv2.resize(background_img[starty : starty + max_dim, startx : startx + max_dim, :], (50, 50))
	final_path = f'./dataset/{sys.argv[2]}/' + shape_name + '/' + str(i) + '.png'
	print(final_path)
	cv2.imwrite(final_path, background_img)
