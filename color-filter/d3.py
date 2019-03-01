import cv2
import numpy as np

frame = cv2.imread('ilk.png', 1)
tt = cv2.imread('ilk.png', 1)
tt2 = cv2.imread('ilk.png', 1)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([10, 10, 10])

upper_red = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame, frame, mask=mask)
mask2=cv2.bitwise_not(mask,None,None);

#res2 = cv2.bitwise_xor(frame,,mask,mask=mask)

print(upper_red,upper_red.dtype,upper_red.shape)







[r,c]= tt.shape[:2]
print(r,c)
r=r-1
c=c-1
dd=1
print(mask[162,260])
for i in range(0,c):
    for j in range(0, r):
        #print(j,i)
        #print(mask[j,i])
        if mask[j,i] == 255:
            dd = dd + 1
            print("girdi")
            print(dd)
            tt[j][i][1] =255
            tt[j][i][0] = 255
            tt[j][i][2] = 255


#res2[159,260,0] = 0
#res2[159,260,1] = 0
#res2[159,260,2] = 0

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
#cv2.imshow('res', res)
cv2.imshow('tt', tt)
cv2.imshow('tt2', tt2)
kt=cv2.imread('kt.png',1)
cv2.imshow('kt', kt)
#cv2.imwrite('kt.png',tt)


k = cv2.waitKey(0)

cv2.destroyAllWindows()

