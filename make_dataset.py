import os

path = './dataset/'

folders = ['train/', 'valid/', 'test/']
sub_directories = ['images/', 'labels/']

count = 0
for dir in sub_directories:
    os.mkdir(path + dir)
    for folder in folders:
        os.mkdir(path + dir + folder)
