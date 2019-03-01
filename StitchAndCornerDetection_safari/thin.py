import cv2
import numpy as np
import math
from simpleai.search import SearchProblem, astar



img=cv2.imread('/home/avesta/Desktop/CalismaDizini/maze.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thin = cv2.ximgproc.thinning(gray, None, cv2.ximgproc.THINNING_ZHANGSUEN)

cv2.imshow(thin)

cv2.waitKey(0)