from scipy import ndimage
from scipy import misc
import numpy as np
face=misc.face()
#misc.imsave('face.png',f)

import matplotlib.pyplot as plt
import cv2

plt.imshow(face)
plt.show()

print(type(face),face.shape,face.dtype)

#############################
print('='*50)

face.tofile('face.raw')
ffr=np.fromfile('face.raw',dtype=np.uint8)
print(ffr.shape)
ffr.shape=face.shape
print(ffr.shape)

#############################
print('='*50)

face_memmap=np.memmap('face.raw',dtype=np.uint8,shape=face.shape)

#for i in range(10):
  # im=np.random.randint(0,256,size=(250,250,3))
  #  cv2.imwrite('random_%02d.png'%i,im)

from glob import glob
filelist = glob('random*.png')
print(filelist)
print(filelist.sort())

#############################
print('='*50)
f2=misc.face()
f=misc.face(gray=True)
plt.imshow(f,cmap="magma")
plt.show()

we,he,zz=f2.shape
print(we,he,zz)
ft=np.zeros(f2.shape,dtype=np.uint8)
#print(ft,ft.shape,ft.ndim,ft.dtype,f.shape,f.ndim,f.dtype)
#print(f2,f2.shape,f2.ndim,f2.dtype,ft.shape,ft.ndim,ft.dtype)
print(ft.shape,ft.ndim,ft.dtype)
ft[:,:,2]=f2[:,:,2]
print(ft.shape,ft.ndim,ft.dtype)
plt.imshow(ft)
plt.show()

#############################
print('='*50)

plt.imshow(f,cmap="hot",vmin=30,vmax=200)
plt.show()
plt.axis('off')

plt.contour(f,[50,200])
plt.show()

plt.imshow(f[320:340,510:530],cmap="hot",interpolation='none')
plt.show()
plt.imshow(f[320:340,510:530],cmap="hot",interpolation='bicubic')
plt.show()

#############################
print('='*50)
