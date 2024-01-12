import cv2 as cv

# *** Reading images ***
# read image
img = cv.imread('Photos/cat_large.jpg')
# show image
cv.imshow('Cat', img)

# wait for specified time in pytms 
cv.waitKey(0)


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# *** Reading Videos ***
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # wait for letter 'd' to stop video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()




