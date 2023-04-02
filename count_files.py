import glob
paths = ['./dataset/images/test/', './dataset/images/train/', './dataset/images/valid/', './dataset/labels/test/', './dataset/labels/train/', './dataset/labels/valid/']
fpaths = list()
for path in paths:
    print(path, len(glob.glob(path + '*.png') + glob.glob(path + '*.jpg') + glob.glob(path + '*.txt')), 'files.')
