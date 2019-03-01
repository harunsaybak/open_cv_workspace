from numpy import *

aa=array([(1,2),(3,4)])
print(aa)

print('*'*20)

a= arange(15).reshape(3,5)
print(a)
print('*'*20)

b= array([2,3,4])
print(b,b.dtype)

print('*'*20)

b=array([(1.5,2,3),(4,5,6)],dtype=int16)
print(b,b.ndim,b.dtype)

print('*'*20)

c=array([[1,2],[3,4]],dtype=int16)
print(c,c.ndim,c.dtype)

print('*'*20)

xx=zeros((3,4),dtype=uint8)
print(xx,xx.dtype)

print('*'*20)

yy = empty((1,2))

print(yy,yy.dtype)

print('*'*20)

x1=arange(10,30,10)
print(x1,x1.dtype)

print('*'*20)

x2=linspace(0,10,5)
f=sin(x2)
#print(x2,x2.dtype)

print('*'*20)

x3=zeros((3,4,2))
print('x3= ',x3,x3.dtype,x3.ndim,x3.size,x3.shape)

print('*'*20)

x4=arange(30).reshape(3,2,5)
x5=x4[0,:,:]
print("x4= ",x4,"***",x5,"xxx",x4[:,:,0])

print('*'*20)
x4=arange(30).reshape(5,6)
print(x4,x4[range(0,3),range(0,3)])

print('*'*20)

print(x4,"\n\n",x4[:,0])

x5=array([(0,1,2,3,4,5),( 5,4,3,8,8,7)])
print(x5)

if  all(x5[1,:])==all(x4[0,:]):
    print("eşit")
else:
    print("değil")

print('*'*20)


foto=

