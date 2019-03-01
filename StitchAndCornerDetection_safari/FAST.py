"""
FAST'ın sadece anahtar nokta tespiti için olduğunu not etmemiz gerekiyor.
Anahtar noktaları tespit edildikten sonra,
tanımlayıcıları hesaplamak için SIFT veya SURF kullanmamız gerekir.
"""

import cv2

import numpy as np

gray=cv2.imread('/home/avesta/Desktop/CalismaDizini/music.jpg',0)

fast = cv2.FastFeatureDetector_create(nonmaxSuppression=False)

keypoints = fast.detect(gray,None)

print("max olmayan bastirma ile anahtar nokta sayisi ", len(keypoints))

# Draw keypoints on top of the input image

img_keypoints_with_nonmax=cv2.drawKeypoints(gray,keypoints,None,(0,255,0))

cv2.imshow('FAST keypoints - without non max suppression', img_keypoints_with_nonmax)
cv2.waitKey(0)

# Disable nonmaxSuppression   bastirma ile anahtar nokta sayisi
fast = cv2.FastFeatureDetector_create(nonmaxSuppression=True)


# tekrar keypointleri bul

keypoints=fast.detect(gray,None)

print("NonmaxSuppression olmadan Toplam Anahtar Noktaları",len(keypoints))

img_keypoints_without_nonmax = cv2.drawKeypoints(gray, keypoints,None,color=(0,255,0))
cv2.imshow('FAST keypoints - without non max suppression', img_keypoints_without_nonmax)
cv2.waitKey(0)




