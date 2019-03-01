#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html?highlight=surf
#https://www.safaribooksonline.com/library/view/opencv-with-python/9781785283932/ch05s06.html

# SIFT dosyasina bakilarak daha anlasilir olur
import cv2
import numpy as np

img=cv2.imread('/home/avesta/Desktop/CalismaDizini/depo.jpg')
img2=img
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# bu kodun calismasi icin opencv-contrib kutuphanesi gerekiyor
surf = cv2.xfeatures2d.SURF_create(15000) # 15000 , Bu eşik, anahtar noktalarının sayısını denetler
#surf.hessianThreshold = 15000  ama bu satir python 3.6 da calismadi o yuzden yukardaki tanimladni
#print(surf.hessianThreshold) buda calismadi



kp, des = surf.detectAndCompute(gray, None)

img = cv2.drawKeypoints(img, kp, None, (0,255,0), 4)

cv2.imshow('SURF features', img)
cv2.waitKey()

