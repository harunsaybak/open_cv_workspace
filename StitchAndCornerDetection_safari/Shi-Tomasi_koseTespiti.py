"""
Takip etmek için iyi özellikler
Harris köşe dedektörü birçok durumda iyi performans gösterir, ancak birkaç şey üzerinde özlüyor. Harris ve Stephens'ın orijinal yazısından yaklaşık altı yıl sonra, Shi-Tomasi daha iyi bir köşe detektörü ile geldi. Orijinal kağıdı http://www.ai.mit.edu/courses/6.891/handouts/shi94good.pdf adresinden okuyabilirsiniz . Genel kaliteyi geliştirmek için farklı bir puanlama işlevi kullandılar. Bu yöntemi kullanarak, verilen görüntüdeki 'N' en güçlü köşeleri bulabiliriz. Bu, görüntüden bilgi çıkarmak için her köşeyi kullanmak istemediğimizde çok kullanışlıdır.

Shi-Tomasi köşe dedektörünü uygularsanız Daha önce gösterilen görüntüye şöyle bir şey göreceksiniz:


"""
import cv2
import numpy as np

img=cv2.imread('/home/avesta/Desktop/CalismaDizini/kup.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kose=cv2.goodFeaturesToTrack(gray,15,0.05,25) # en iyi 15 tane koseyi bulacak
"""
cv2.goodFeaturesToTrack(gray,maxCorners,qualityLevel,minDistance)

qualityLevel - Görüntü köşelerinin minimum kabul edilen kalitesini karakterize eden parametre. 
Parametre değeri, minimum özdeğeri (bkz. CornerMinEigenVal () ) 
veya Harris işlev yanıtı olan en iyi köşe kalitesi ölçüsü ile çarpılır (bkz. CornerHarris () ).
Üründen daha düşük kalite ölçüsü olan köşeler reddedilir. 
Örneğin, en iyi köşe kalite ölçüsü = 1500 ve qualityLevel = 0.01 ise, 
kalite ölçüsü 15'ten küçük olan tüm köşeler reddedilir.

minDistance - Döndürülmüş köşeler arasındaki minimum Euclidean mesafesi.
"""
kose=np.float32(kose)

for i in kose :
    x , y = i[0]
    cv2.circle(img,(x,y),4,255,2)

cv2.imshow("Top 'k' features",img)
cv2.waitKey()