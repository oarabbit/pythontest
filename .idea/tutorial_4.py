import cv2 as cv
import numpy as np


def inverse(image):
    dst = cv.bitwise_not(image)
    # 0变成1,1变成0，像素取反
    cv.imshow("inverse demo",dst)


src = cv.imread("E:/cat.jpg")
cv.namedWindow("input image", cv.WINDOW_NORMAL)
cv.imshow("input image", src)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1)*1000/cv.getTickFrequency()
print("time: %s" % time)
cv.waitKey(0)
cv.destroyAllWindows()