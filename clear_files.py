import os

path = './dataset/'

folders = ['train/', 'valid/', 'test/']
sub_directories = os.listdir('dataset/train/')#['images/', 'labels/']

count = 0
for dir in folders:
    for folder in sub_directories:
        fpath = path + dir + folder
        for file in os.listdir(fpath):
            os.remove(fpath + '/' + file)
            count += 1
print(f'Cleared {count} files.')
