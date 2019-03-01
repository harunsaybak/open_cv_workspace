from scipy import misc
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

######## GAUS FİLTER #########
print("="*50)
print("="*50)
face=misc.face(gray=True)

blurred=scipy.ndimage.gaussian_filter(face,sigma=5)

plt.imshow(blurred,cmap='gray')
plt.show()

######## UNİFORM FİLTER #########
print("="*50)
print("="*50)

local_mean=scipy.ndimage.uniform_filter(face,size=11)
plt.imshow(local_mean,cmap='gray')
plt.show()