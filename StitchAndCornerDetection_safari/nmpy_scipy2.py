from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
face=misc.face()
#misc.imsave('face.png',f)


import cv2

face=misc.face(gray=True)
#print(face[100:120])
lx,ly=face.shape
#############################
print('='*50)
print('='*50)

X,Y=np.ogrid[0:lx,0:ly]
#print(X,Y)
mask=(X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
print("mask=",mask)
face[mask]=0
face[range(400),range(400)]=255
plt.imshow(face,cmap='gray')
plt.show()

#############################
print('='*50)
print('='*50)

face2=misc.face(gray=True)
crop_face2=face2[lx//4: -lx//4,ly//4:-ly//4]
print(crop_face2.dtype,crop_face2.shape,crop_face2.ndim)
plt.imshow(crop_face2)
plt.show()

