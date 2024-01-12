import cv2 as cv

# *** Reading images ***
# read image
# img = cv.imread('Photos/cat.jpg')
# show image
# cv.imshow('Cat', img)
# wait for specified time in pytms 
# cv.waitKey(0)


# *** Reading Videos ***
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # wait for letter 'd' to stop video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


