import os

path = './dataset/'

folders = ['train/', 'valid/', 'test/']
sub_directories = ['images/', 'labels/']

count = 0
for dir in sub_directories:
    for folder in folders:
        fpath = path + dir + folder
        for file in os.listdir(fpath):
            os.remove(fpath + file)
            count += 1
print(f'Cleared {count} files.')
