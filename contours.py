import cv2 as cv
import numpy as np 

# Read image
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# *** Detectavimas naudojant Canny funkcija ***
# Blur image (kad sumazinti krastiniu skaiciu)
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)
# *** Detectavimas naudojant Canny funkcija END ***

# *** Kitas variantas ***
ret, thresh = cv. threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


# Find contours
countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)} contour(s) found!')


cv.drawContours(blank, countours, -1, (0,0,255), 1)
cv.imshow('Countour Drawn', blank)


cv.waitKey(0)