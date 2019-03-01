import cv2
import numpy as np

"""

stitcher = cv2.createStitcher(False)
foo = cv2.imread("/home/avesta/Desktop/CalismaDizini/jur.jpeg", cv2.IMREAD_COLOR)
bar = cv2.imread("/home/avesta/Desktop/CalismaDizini/xar.jpeg", cv2.IMREAD_COLOR)
result = stitcher.stitch((foo,bar))

cv2.imwrite("result.png", result[1])

"""
images = []
images.append(cv2.imread('/home/avesta/Desktop/CalismaDizini/xx.jpeg', cv2.IMREAD_COLOR))
images.append(cv2.imread('/home/avesta/Desktop/CalismaDizini/xy.jpeg', cv2.IMREAD_COLOR))
#images.append(cv2.imread('/home/avesta/Desktop/CalismaDizini/3.png', cv2.IMREAD_COLOR))
#images.append(cv2.imread('/home/avesta/Desktop/CalismaDizini/4.png', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:
    #cv2.imwrite('foto.jpeg',pano)
    cv2.imshow('panorama', pano)
    cv2.waitKey()

    cv2.destroyAllWindows()
else:
    print('Error during stiching')

