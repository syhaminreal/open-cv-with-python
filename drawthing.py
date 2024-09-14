import cv2 as cv
import numpy as np

# Create a blank image or space
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a certain color
blank[200:300, 300:400] = 0, 225, 0
cv.imshow('Green', blank)

# Draw a rectangle over it
cv.rectangle(blank, (0,0), (225,225), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,225), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,225), thickness=3)
cv.imshow('Line', blank)


# Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,225), thickness=3)
cv.imshow('Line', blank)
#write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 225, 0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)
