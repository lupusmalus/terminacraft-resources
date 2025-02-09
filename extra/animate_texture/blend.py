from __future__ import print_function
import cv2 as cv
import numpy as np
import imutils
import time

# [load]
img1 = cv.imread(cv.samples.findFile('discoball_lowres.png'))

img2 = img1.copy()
np.random.shuffle(img2) 

res = img1.copy()

for i in range(63):
        # alpha = j * 4
        # beta = 1.0 - alpha
        # img3 = cv.addWeighted(img1, beta, img2, alpha, 0.0)
    res = cv.vconcat([res, img2])
    img1 = img2.copy()
    np.random.shuffle(img2) 

res = imutils.resize(res, width=64, inter = cv.INTER_LINEAR)
cv.imwrite('C:\\Users\\wengl\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft\\assets\\minecraft\\textures\\mm\\blocks\\discoballres.png', res)

    


