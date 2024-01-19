import cv2 as cv 

# image of 1 person
# img = cv.imread('Photos/lady.jpg')
# cv.imshow('Person', img)

#image with people group
img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group of people', img)

# convert to gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# read and store info
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# recongnise faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

# draw rectange over the faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)


cv.waitKey(0)