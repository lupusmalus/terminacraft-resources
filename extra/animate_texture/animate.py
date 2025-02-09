import cv2
import numpy as np
import argparse


def transpose(img, dir):
    if dir == 'l':
        return np.roll(img, shift=-1, axis=1)
    elif dir == 'r':
        return np.roll(img, shift=1, axis=1)
    elif dir == 'u':
        return np.roll(img, shift=-1, axis=0)
    elif dir == 'd':
        return np.roll(img, shift=1, axis=0)
    else:
        raise ValueError("Direction argument must be one of [l, u, r, d]")



parser = argparse.ArgumentParser()
parser.add_argument("dir", help="direction to animate along (l, r , u d)")
parser.add_argument("src_img", help="filepath of image to animate")
parser.add_argument("dest_img", help="Name of output image")
args = parser.parse_args()


img = cv2.imread(args.src_img, cv2.IMREAD_UNCHANGED)
height, width = img.shape[:2]
res = img
dir = args.dir

if dir in ('l', 'r'):
    lim = width
else:
    lim = height


for i in range(lim - 1):
    img = transpose(img, dir)
    res = cv2.vconcat([res, img])

cv2.imwrite(args.dest_img, res)