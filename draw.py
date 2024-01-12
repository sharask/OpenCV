import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

cv.waitKey(0)