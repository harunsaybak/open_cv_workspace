# https://www.linkedin.com/pulse/sift-transforms-rohan-verma/
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import cv2
import numpy as np

img=cv2.imread('/home/avesta/Desktop/CalismaDizini/depo.jpg')
img2=img
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

keypoints= sift.detect(gray,None) # bu kodun calismasi icin opencv-contrib kutuphanesi gerekiyor
#yukardaki kod koseleri bulur
cv2.drawKeypoints(img,keypoints,img2,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# img: islem yailacak foto, keypoint:koseler, img2: sonuc,flags: Bu işlev, çıktı görüntüsündeki iki görüntüden anahtar nokta eşleşmelerini çizer. Eşleşme, iki anahtar noktasını (daire) birbirine bağlayan bir çizgidir.
"""
sift.detect () işlevi, resimlerdeki anahtar noktasını bulur. 
Görüntünün yalnızca bir bölümünü aramak istiyorsanız bir maskeyi geçirebilirsiniz. 
Her anahtar nokta, (x, y) koordinatları, 
anlamlı mahallenin boyutu, yönünü belirten açı, 
anahtar noktaların gücünü belirleyen yanıt gibi birçok özelliğe sahip olan özel bir yapıdır.

OpenCV ayrıca, kilit noktaları konumlarında küçük daireler çizen cv2.drawKeyPoints () işlevini sağlar .
Bir bayrağı geçirirseniz, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS , 
anahtar noktası büyüklüğünde bir daire çizecektir ve hatta yönünü gösterecektir. 


kp, des = sift.detectAndCompute (gray, None )
Burada kp, anahtar noktaların bir listesi olacaktır ve des, sayısal bir şekil dizisidir.

Bu yüzden anahtar noktaları, tanımlayıcılar vb. Var. 
Şimdi farklı görüntülerde anahtar noktaların nasıl eşleştirileceğini görmek istiyoruz.
İstediğiniz makaleler bu anahtar noktaların nasıl eşleştirileceğini ele alacaktır.
"""


cv2.imshow('SIFT features',img2)
cv2.waitKey()




