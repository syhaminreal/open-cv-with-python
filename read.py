import cv2 as cv

# Read the image
img = cv.imread('Photo/mali.jpg')

# Display the image in a window
cv.imshow('mali', img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

# Destroy all OpenCV windows
cv.destroyAllWindows()
