import cv2
import numpy as np
import sys

# You should replace these 3 lines with the output in calibration step
DIM=(4032, 3024)
K=np.array([[2864.882687817586, 0.0, 1994.751942503189], [0.0, 2849.940560075939, 1447.3227396725856], [0.0, 0.0, 1.0]])
D=np.array([[0.011437616232410689], [-1.537417381111993], [5.151598339492198], [-4.968587608331246]])

def undistort(img_path):
	img = cv2.imread(img_path)
	h,w = img.shape[:2]
	map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
	undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
	cv2.imshow("undistorted", undistorted_img)
	cv2.imwrite("test.png",undistorted_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	#for p in sys.argv[1:]:
	undistort("2018_0905_170548_003.JPG")


