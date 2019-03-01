import numpy as np
import cv2
from matplotlib import pyplot as plt

img1=cv2.imread('/home/avesta/Desktop/CalismaDizini/tır.jpg')

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2=cv2.imread('/home/avesta/Desktop/CalismaDizini/tır2.jpg')

img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 20 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,None,None,None,2)
#img3 = cv2.drawMatches(img1,kp1,img2,kp2, , matches[:10], flags=2)
plt.imshow(img3),plt.show()




