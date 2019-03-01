import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('/home/avesta/Desktop/CalismaDizini/kup.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)

dst=cv2.cornerHarris(gray,4,5,0.04) # sadece keskin koseleri algilar
# parametreler ici https://docs.opencv.org/3.0-beta/modules/imgproc/doc/feature_detection.html#void%20cornerHarris(InputArray%20src,%20OutputArray%20dst,%20int%20blockSize,%20int%20ksize,%20double%20k,%20int%20borderType)
#dst = cv2.cornerHarris(gray, 14, 5, 0.04)    # to detect soft corners


dst=cv2.dilate(dst,None)

img[dst>0.015*dst.max()]=[0,0,0] # 0.015 esik degerdir fotodan fotoya degisir

cv2.imshow('harris',img)
cv2.waitKey()