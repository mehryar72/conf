import glob
import torch
from torch.utils.data import Dataset
import os
import sys
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageOps, ImageChops, ImageFilter
import numbers
import random
from itertools import islice
from random import shuffle
import math
import pickle
import csv
import torchvision.transforms as transforms
from pathlib import Path
import math
import cv2
import time

# root='C:\\Users\\abbas\\OneDrive\\Documents\\makehuman\\v1py3\\grab\\New folder (2)\\'
#
# image_big=np.zeros((1500,1500,3),dtype=np.uint8)
# image_big2=np.zeros((1500,1500,3),dtype=np.uint8)
#
# imgf=glob.glob(root+'*.png')
# i=0
# for c,fol in enumerate(imgf):
#     if c<9:
#         i=c
#         b=i%3
#         d=int(i/3)
#
#         image=cv2.imread(fol)
#         image_big[b*500:b*500+500,d*500:d*500+500,:]=image
#     else:
#         i = c - 9
#         b = i % 3
#         d = int(i / 3)
#
#         image = cv2.imread(fol)
#         image_big2[b * 500:b * 500 + 500, d * 500:d * 500 + 500, :] = image
#
#
# cv2.imwrite(root+'imgB1.png',image_big)
# cv2.imwrite(root+'imgB2.png',image_big2)
image = Image.open('C:\\Users\\abbas\\OneDrive\\Documents\\makehuman\\v1py3\\grab_cropped\\1\\images_2020-11-28_16_48_35_25_Ya_0_Za_0_mod0010_EyesRLnChinUppernMouthLowernBrowlower\\25.jpeg')
transforms=[transforms.RandomPerspective(distortion_scale=0.1, p=0.5),
                transforms.RandomAffine(5, translate=(0.05, 0.05), scale=None, shear=5, resample=Image.NEAREST,
                                                               fillcolor= 0),
                transforms.RandomResizedCrop(160, scale=(0.80, 1.20), ratio=(0.80, 1.20)),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1)]

root='C:\\Users\\abbas\\OneDrive\\Documents\\makehuman\\v1py3\\grab\\New folder (3)\\'
for c,trans in enumerate(transforms):
    im=trans(image)
    im.save(root+'{}.png'.format(c))
