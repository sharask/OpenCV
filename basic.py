import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur )

# Edge Cascade
canny = cv.Canny(img, 125, 125)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilated', dilated)

cv.waitKey(0)