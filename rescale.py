import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading the videos
capture = cv.VideoCapture('video/x.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    frame_resized = rescaleFrame(frame, scale=0.2)


    cv.imshow('Video', frame)
    cv.imshow('Rescaled Video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
