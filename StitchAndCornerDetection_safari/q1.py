from scipy import misc
face=misc.face()
misc.imsave('face.png',face)

face=misc.imread('face.png')
print(type(face),face.shape,face.dtype)


