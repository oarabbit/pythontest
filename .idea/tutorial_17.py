import cv2 as cv
import numpy as np


# 图像二值化 0白色 1黑色
# 全局阈值
def threshold_image(image):
    # 图像灰度化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("image", gray)

    # 全局自适应阈值 参数0可改为任意数字但不起作用
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value is：%s" % ret)
    cv.imshow("binary", binary)

    # TRIANGLE法，全局自适应阈值
    # 参数0可改为任意数字但不起作用，适用于单个波峰
    # 图像的信息丢失
    ret, binary = cv.threshold(gray, 0, 255,
                               cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value is：%s" % ret)
    cv.imshow("TRIANGLE", binary)

    # 自定义阈值为150,大于150的是白色,小于的是黑色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    print("threshold value is：%s" % ret)
    cv.imshow("binary", binary)

    # 自定义阈值为150,大于150的是黑色,小于的是白色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
    print("threshold value is：%s" % ret)
    cv.imshow("binary", binary)

    # 截断1
    # 大于150的是改为150  小于150的改为0
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)
    print("threshold value is：%s" % ret)
    cv.imshow("binary", binary)

    # 截断2
    # 小于150的是改为0  大于150的改为150
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)
    print("threshold value is：%s" % ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("原来", gray)
    binary1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("局部1", binary1)
    binary2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)#高斯处理
    cv.imshow("局部2", binary2)


src = cv.imread("E:/Eurus.jpg")
threshold_image(src)
cv.waitKey(0)
cv.destroyAllWindows()