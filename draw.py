import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

 # Paint a square inside the image
blank[:] = 0, 0, 0
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red Square', blank)

#2. Paint a Rectangle
blank[:] = 0, 0, 0
cv.rectangle(blank, (10,10), (250,350), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)


# Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)