import cv2 as cv
import numpy as np

#create a blank image or space
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#paint  the image a certain color
blank[200:300, 300:400] = 0, 225, 0
cv.imshow('Green', blank)

#2. draw a rectangle over it
cv.rectangle(blank, (0,0), (225,225), (0,255,0), thickness =2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
