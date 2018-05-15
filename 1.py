import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread

filepath = '/home/JPEGImages'  # 数据集目录
pathDir = os.listdir(filepath)

R_channel = 0
G_channel = 0
B_channel = 0
for idx in xrange(len(pathDir)):
    filename = pathDir[idx]
    img = imread(os.path.join(filepath, filename))
    R_channel = R_channel + np.sum(img[:, :, 0])
    G_channel = G_channel + np.sum(img[:, :, 1])
    B_channel = B_channel + np.sum(img[:, :, 2])

num = len(pathDir) * 384 * 512
R_mean = R_channel / num
G_mean = G_channel / num
B_mean = B_channel / num

print("R_mean is %f, G_mean is %f, B_mean is %f" % (R_mean, G_mean, B_mean))