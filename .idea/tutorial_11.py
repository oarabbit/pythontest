import cv2 as cv
import numpy as np


# 截取图片中的指定区域或在指定区域添加某一图片
def jie_image(src):
    # 截取区域：高度，宽度
    src1 = src[50:100, 50:100]
    cv.imshow("src1", src1)
    # 灰色
    gray = cv.cvtColor(src1,cv.COLOR_BGR2GRAY)
    src2 = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    # 指定位置填充，大小要一样才能填充
    src[50:100, 50:100] = src2
    cv.imshow("src", src)


src = cv.imread("E:/cat.jpg")
cv.imshow("image", src)
jie_image(src)
cv.waitKey(0)
cv.destroyAllWindows()