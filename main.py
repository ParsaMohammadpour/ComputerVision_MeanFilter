# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_J6bWj2tTB_Zfoc22IIkD2P-QTm7_2wx
"""

pip install mahotas

import cv2
from google.colab.patches import cv2_imshow
import numpy as np
import mahotas

from google.colab import drive
drive.mount('/content/drive')

def load_image(path):
  original_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  cv2_imshow(original_img)
  return original_img

path = '/content/drive/MyDrive/Computer Vision/Fig0333(a)(test_pattern_blurring_orig).tif'
img = load_image(path)
# print(img[100])
# n = 3
# new_img = mahotas.mean_filter(img, n)
# cv2_imshow(new_img)
# print(new_img[100])
# n = 5
# new_img = mahotas.mean_filter(img, n)
# cv2_imshow(new_img)
# print(new_img[100])
# n = 7
# new_img = mahotas.mean_filter(img, n)
# cv2_imshow(new_img)
# print(new_img[100])
arr = np.arange(25).reshape(5, 5)
print(arr)
# print('****************************************')
# print(mahotas.mean_filter(arr, 3))
# print('****************************************')
# print(mahotas.mean_filter(arr, 5))
print(mahotas.mean_filter(arr, 3) - mahotas.mean_filter(arr, 5))