from scipy import misc
import cv2
import numpy as np
import matplotlib.pyplot as plt

foto=misc.face(gray=True)

plt.imshow(foto,cmap='gray')
plt.show()


new1=foto[:,0:600]
new2=foto[:,450:]
print(new1.shape,new1.dtype,new2.shape,new2.dtype)

plt.imshow(new2,cmap='gray')

plt.figure(2)
plt.imshow(new1,cmap='gray')
plt.show()

ilksutun=new2[:,0].reshape(-1,1)
#print(ilksutun,ilksutun.shape)

print('='*100)
deger=new1[:,11].reshape(-1,1)
#print(deger.shape)
#print(deger[3,0])

j=0
#while j<767:

 #   if deger[j,0]!=ilksutun[j,0]:
  #      print("eşit değil")
  #  j+=1

i=1
k=0
while i<600:
    DD=new1[:, i].reshape(-1,1)
    print(DD.shape,ilksutun.shape)
    print(i)
    if any(DD.reshape(-1,1))!=any(ilksutun.reshape(-1,1)):
        k=i
        print("="*100,"="*100,"="*100,"="*100,ilksutun,"="*100,"="*100,"="*100,"="*100,DD,"girdi")
        break
    i+=1

print(k)