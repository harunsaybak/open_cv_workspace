import cv2
import numpy as np

image=cv2.imread('/home/avesta/Desktop/CalismaDizini/maze.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#cv2.imshow('gray',gray)
#cv2.waitKey(0)

thn=cv2.ximgproc.thinning(gray,None,cv2.ximgproc.THINNING_ZHANGSUEN)

cv2.imshow('thn',thn)
cv2.waitKey(0)

i=0
while i<242:
    j=0
    while j<242:
        if thn[i,j]==255:
            image[i,j,2]=255
            image[i, j,1]=0
            image[i, j,0]=0
        j=j+1
    i=i+1


#cv2.imwrite('ima.png',image)

cv2.imshow('son',image)
cv2.waitKey(0)

