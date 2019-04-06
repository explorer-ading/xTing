#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/46267443/merge-images-using-opencv-and-a-mask

import numpy as np
import cv2
from matplotlib import pyplot as plt

img1=np.random.rand(100,100,3)
img2=np.random.rand(100,100,3)
mask=np.random.rand(100,100)>.5

plt.imshow(img1)
plt.imshow(img2)

## Mask Approach-1
comb_img=img2.copy()
comb_img[mask]=img1[mask]

## Mask Approach-2
comb_img = np.zeros_like(img1)
comb_img[mask] = img1[mask]
comb_img[~mask] = img2[~mask]


# https://stackoverflow.com/questions/7589012/combining-two-images-with-opencv
# horizon concatenate
comb_img = np.concatenate((img1, img2), axis=0)
# vertical concatenate
comb_img = np.concatenate((img1, img2), axis=1)


# https://stackoverflow.com/questions/50472180/match-two-images-keypoints
# ...


## Output 
cv2.imwrite("00.png",comb_img)


