import cv2 as cv

# Open the video file
capture = cv.VideoCapture('video/x.mp4')

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()
    
    # If the frame was not retrieved successfully, break the loop
    if not isTrue:
        break

    # Display the frame in a window
    cv.imshow('Video', frame)

    # Wait for 20 ms and break the loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object
capture.release()

# Destroy all OpenCV windows
cv.destroyAllWindows()
