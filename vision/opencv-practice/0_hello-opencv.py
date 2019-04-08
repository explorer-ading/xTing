#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena-465x465.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


img = cv2.imread('lena-465x465.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


#cv2.imshow('image',img)
#k = cv2.waitKey(0)
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv2.imwrite('messigray.png',img)
#    cv2.destroyAllWindows()


cv2.imwrite('cv2-output.png',img)


