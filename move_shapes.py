import os

path = './finished_shapes_2/'
files = os.listdir(path)

for fname in files:
    if 'modified' in fname:
        shape = fname[:fname.find('_')]
        final_dest = './dataset/images/train/' + shape + '/' + fname
        #print(final_dest)
        os.rename(path + fname, final_dest)
