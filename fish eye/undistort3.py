import cv2
import numpy as np
import sys

"""
DIM=(2592, 1944)
K=np.array([[1831.4519963389344, 0.0, 1340.2030310863213], [0.0, 1833.4685115702734, 976.5193948312334], [0.0, 0.0, 1.0]])
D=np.array([[0.07369660158975364], [-1.2653296183311125], [3.4563463517035147], [-3.2796319518115884]])
"""

DIM=(4032, 3024)
K=np.array([[2896.912980324403, 0.0, 2021.8177163509927], [0.0, 2883.891359397373, 1514.0065826908574], [0.0, 0.0, 1.0]])
D=np.array([[-0.072868600156874], [-0.4470076410114109], [1.6081442644439954], [-1.9347833569359192]])
bb=0.0

def undistort(img_path, balance=bb, dim2=None, dim3=None):
    img = cv2.imread(img_path)
    dim1 = img.shape[:2][::-1]  #dim1 is the dimension of input image to un-distort
    assert dim1[0]/dim1[1] == DIM[0]/DIM[1], "Image to undistort needs to have same aspect ratio as the ones used in calibration"
    if not dim2:
        dim2 = dim1
    if not dim3:
        dim3 = dim1
    scaled_K = K * dim1[0] / DIM[0]  # The values of K is to scale with image dimension.
    scaled_K[2][2] = 1.0  # Except that K[2][2] is always 1.0
    # This is how scaled_K, dim2 and balance are used to determine the final K used to un-distort image. OpenCV document failed to make this clear!
    new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, D, dim2, np.eye(3), balance=balance)
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, np.eye(3), new_K, dim3, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    cv2.namedWindow("undistorted",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("undistorted",700,700)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    for ii in range(15):
        bb = bb+0.3
        for p in sys.argv[1:]:
            #bb = bb + 0.2
            undistort(p,bb)
