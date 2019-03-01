import cv2
import numpy as np

img=cv2.imread('/home/avesta/Desktop/CalismaDizini/depo.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#start ORB
orb =   cv2.ORB_create()

#find keypoints with ORB

kp  =   orb.detect(gray,None)

#compute(hesapla) the descriptors(tanimlayici) with ORB

kp , des    =   orb.compute(gray,kp)

# draw only the location of the keypoints without size or orientation

final_keypoints = cv2.drawKeypoints(img, kp,None, color=(0,255,0), flags=0)

cv2.imshow('ORB keypoints',final_keypoints)
cv2.waitKey(0)