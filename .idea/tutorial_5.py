import cv2 as cv
import numpy as np


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    # RGB转换为gray
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    # RGB转换为hsv
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    # RGB转换为yuv
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    # RGB转换为ycrcb
    cv.imshow("Ycrcb",ycrcb)


src = cv.imread("E:/cat.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()