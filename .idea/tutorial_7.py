import cv2 as cv
import numpy as np


src = cv.imread("E:/cat.jpg")
cv.namedWindow("input image",cv.WINDOW_NORMAL)
cv.imshow("input image",src)

b,g,r = cv.split(src)
# 通道分离
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

src[:,:,2] = 0
# 最后一个通道赋为0
cv.imshow("channel images",src)

src[:,:,2] = 0
src = cv.merge([b,g,r])
# 通道合并，需要传入一个数组
cv.imshow("merge image",src)


cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,Python!")