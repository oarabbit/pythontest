import cv2 as cv
import numpy as np


def shu_image(src1, src2):
    # 数值运算：加减乘除
    src = cv.add(src1, src2)
    # 加：黑色的值为0，超过255默认255，所以是叠加
    cv.imshow("add", src)
    src = cv.subtract(src1, src2)
    # 减：小于0 默认为0
    cv.imshow("subtract", src)
    src = cv.divide(src1, src2)
    # 乘
    cv.imshow("divide", src)
    src = cv.multiply(src1, src2)
    # 除
    cv.imshow("multiply", src)


# 通道的均值和标准差（像素差异大小）
def others(m1,m2):
    M1,dev1 = cv.meanStdDev(m1)
    M2,dev2 = cv.meanStdDev(m2)
    # 求出宽和高
    h,w = m1.shape[:2]
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)
    # 大小h*w，三个通道，每个RGB通道是一个矩阵，全0矩阵
    img = np.zeros([h,w],np.unit8)
    # 三个通道都为0
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)

src1 = cv.imread("E:\pic01.jpg")
src2 = cv.imread("E:\pic02.jpg")
cv.imshow("image1", src1)
cv.imshow("image2", src2)
shu_image(src1, src2)
others(M1,M2)
cv.waitKey(0)
cv.destroyAllWindows()