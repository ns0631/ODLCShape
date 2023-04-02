import os, random, sys, time, base64, json, cv2
import star, cross, trapezoid, circle, rectangle, regular_polygon
from general import *
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFile
from pathlib import Path
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True

class generate:
    def __init__(self, rectangles, image, center):
        #self.number = number
        self.image = image
        self.width, self.height = self.image.size
        self.center = center

        self.selection()

        if self.shape_name == 'circle':
            points = circle.arc(self.center, 360, self.radius)
        elif self.shape_name == 'semicircle':
            points = circle.arc(self.center, 180, self.radius)
        elif self.shape_name == 'quarter_circle':
            points = circle.arc(self.center, 90, self.radius)
        elif self.shape_name == 'trapezoid':
            base = random.randint(20, 30)
            top = int(base * random.uniform(0.3, 0.7))
            height = random.randint(10, 20)
            points = trapezoid.trapezoid(base, top, height, self.center[0], self.center[1], self.width, self.height)
        elif self.shape_name == 'star':
            points = star.star(self.radius, self.center[0], self.center[1])
        elif self.shape_name == 'cross':
            points = cross.cross(self.radius, self.center[0], self.center[1])
        elif self.shape_name == 'rectangle':
            rect_width = random.uniform(20, 30)
            rect_height = int(rect_width * random.uniform(0.3, 0.7))
            points = rectangle.rectangle(rect_width, rect_height, self.center[0], self.center[1],
                                                 self.width, self.height)
        else:
            number_of_sides = side_number[self.shape_name]
            points = regular_polygon.regular_polygon(number_of_sides, self.radius, self.center[0], self.center[1])

        self.points = points

        self.rotate()
        self.compute_bounding_box()
        if 'circle' in self.shape_name:
            middle_x = ( self.max_x + self.min_x ) / 2
            middle_y = ( self.max_y + self.min_y ) / 2
            self.center = ( middle_x, middle_y )

    def compute_bounding_box(self):
        min_x = min(self.points, key=lambda tup: tup[0])[0]
        min_y = min(self.points, key=lambda tup: tup[1])[1]
        max_x = max(self.points, key=lambda tup: tup[0])[0]
        max_y = max(self.points, key=lambda tup: tup[1])[1]

        self.max_x = max_x
        self.min_x = min_x

        self.max_y = max_y
        self.min_y = min_y

        self.bounding_box = [ (min_x, min_y), (max_x, max_y),
                             (max_x, min_y), (min_x, max_y) ]

    def rotate(self):
        rotated_points = list()
        for point in self.points:
            new_point = rotate_point(point, self.tilt, self.center, self.width, self.height)
            rotated_points.append(new_point)
        self.points = rotated_points

    def selection(self):
        self.number = random.randint(0, len(texts) - 1)
        max_shape_index = len(shapes) - 1
        max_color_index = len(colors) - 1

        self.shape_name = shapes[random.randint(0, max_shape_index)]

        self.shape_color = colors[random.randint(0, max_color_index)]
        self.text_color = colors[random.randint(0, max_color_index)]
        while self.text_color == self.shape_color:
            self.text_color = colors[random.randint(0, max_color_index)]

        self.letter = texts[self.number]

        self.radius = random.randint(20, 30)
        self.center = ( random.randint(100, self.width - 100), random.randint(100, self.height - 100) )
        self.tilt = random.randint(0, 359)

def draw(image, handle, shape, shape_color, text_color, outline_color):
    handle.polygon(shape.points, fill=shape_color, outline=outline_color)

    font_file_name = f"../Fonts/{random.choice(font_list)}"
    font = ImageFont.truetype(font_file_name, round(((shape.max_y - shape.min_y) * 2) / 4))
    txt_width, txt_height = font.getsize(shape.letter)

    txt_img = Image.new('RGBA', (txt_width, txt_height), (0, 0, 0, 0))
    draw_txt = ImageDraw.Draw(txt_img)
    draw_txt.text((0, 0), text=shape.letter, font=font, fill=text_color)

    txt_img = txt_img.rotate(shape.tilt, expand=1)

    px, py = (int(shape.center[0] - (shape.max_x - shape.min_x) / 4), int(shape.center[1] - (shape.max_y - shape.min_y) / 4))
    sx, sy = txt_img.size
    coordinates = (px, py, px + sx, py + sy)
    image.paste(txt_img, coordinates, txt_img)

    return {'min_x': px, 'max_x': px + sx, 'min_y': py, 'max_y': py + sy}

background_list = os.listdir('../backgrounds')
if '.DS_Store' in background_list:
    background_list.remove('.DS_Store')

font_list = os.listdir('../Fonts')
if '.DS_Store' in font_list:
    font_list.remove('.DS_Store')

def main():
    global count
    #base_number = int(sys.argv[1]) + 1
    img_dir = f'../dataset/images/{sys.argv[2]}/'
    base_number = len(os.listdir(img_dir)) + 1
    GEN = int(sys.argv[1])
    for i in range(GEN):
        # Get image attributes, resize
        image = Image.open(f"../backgrounds/{random.choice(background_list)}")
        width, height = image.size
        mask_background = np.zeros(height * width).reshape(height, width)
        number_of_shapes = random.randint(0, 10)

        print(f'Image number: {i}')

        background = Image.fromarray(mask_background).convert('RGB')
        background_handle = ImageDraw.Draw(background)
        draw_handle = ImageDraw.Draw(image)

        name = str(base_number + i) + ".jpg"
        center = [ width // 2, height // 2 ]

        img_path = f'../dataset/images/{sys.argv[2]}/' + name
        annotation_path = f'../dataset/labels/{sys.argv[2]}/' + name[:-3] + 'txt'

        annotation = open(annotation_path, 'w')

        shape = generate([], image, center)
        text_corners = draw(image, draw_handle, shape, shape.shape_color, shape.text_color, shape.shape_color)
        annotation_path = annotation_path[:-3] + 'txt'

        shape_corners = {'min_x': shape.min_x - 20, 'min_y': shape.min_y - 20, 'max_x': shape.max_x + 20, 'max_y': shape.max_y + 20}
        relative_center_x = ( ( shape_corners['max_x'] + shape_corners['min_x'] ) / 2 ) / width
        relative_center_y = ( ( shape_corners['max_y'] + shape_corners['min_y'] ) / 2 ) / height
        relative_width = ( shape_corners['max_x'] - shape_corners['min_x'] ) / width
        relative_height = ( shape_corners['max_y'] - shape_corners['min_y'] ) / height

        annotation.write(f'{shapes.index(shape.shape_name)} 0.5 0.5 0.4 0.4\n')

        #annotation.write(f'0 {relative_center_x} {relative_center_y} {1.5 * relative_width} {1.5 * relative_height}\n')
        image = image.crop((shape_corners['min_x'], shape_corners['min_y'], shape_corners['max_x'], shape_corners['max_y'])).resize((80, 80))
        image.save(img_path, 'JPEG')
        annotation.close()

        #print(img_path)

print('Starting', sys.argv[1])
main()
print('Finished with', sys.argv[1])
