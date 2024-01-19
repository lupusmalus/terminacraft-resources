from __future__ import print_function
import cv2 as cv
import numpy as np
import imutils
import time

# [load]
img1 = cv.imread(cv.samples.findFile('C:\\Users\\wengl\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft\\assets\\minecraft\\textures\\mm\\blocks\\discoball_lowres.png'))

img2 = img1.copy()
np.random.shuffle(img2) 

res = img1.copy()
res = cv.GaussianBlur(res, (5,5), 0)
res = imutils.resize(res, width = 64, inter = cv.INTER_LINEAR)

for i in range(16):

    img1_blur = cv.GaussianBlur(img1, (5,5), 0)
    img2_blur = cv.GaussianBlur(img2, (5,5), 0)

    img1_big = imutils.resize(img1_blur, width = 64, inter = cv.INTER_LINEAR)
    img2_big = imutils.resize(img2_blur, width = 64, inter = cv.INTER_LINEAR)
    for j in range(4):
        alpha = j * 0.25
        beta = 1.0 - alpha



        img3 = cv.addWeighted(img1_big, beta, img2_big, alpha, 0.0)
        if i + j > 0:
            res = cv.vconcat([res, img3])
    img1 = img2.copy()
    np.random.shuffle(img2) 

cv.imwrite('C:\\Users\\wengl\\AppData\\Roaming\\.minecraft\\resourcepacks\\terminacraft\\assets\\minecraft\\textures\\mm\\blocks\\discoballres.png', res)

    


