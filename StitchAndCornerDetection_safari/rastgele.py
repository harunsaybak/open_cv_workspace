import cv2
import numpy as np

im = cv2.imread('/home/avesta/Desktop/CalismaDizini/maze.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (0,255,0), 1)

cv2.imshow('ds',im)
cv2.waitKey(0)
