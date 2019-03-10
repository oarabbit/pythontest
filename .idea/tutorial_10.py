import cv2 as cv
import numpy as np


# 粗略的调节对比度(c)和亮度(brightness)
def contrast_brightness_image(src, c, b):
    # 获取shape的数值，height和width、通道
    h, w, ch = src.shape
    # 新建全零图片数组blank,将height和width，类型设置为原图片的格式(色素全为零，输出为全黑图片)
    blank = np.zeros([h, w, ch], src.dtype)
    # 前4个是两张要合成的图片及它们所占比例，第5个double gamma起微调作用
    # 第6个OutputArray dst是合成后的图片，第七个输出的图片的类型（可选参数，默认-1）
    dst = cv.addWeighted(src, c, blank, 1 - c, b)
    cv.imshow("con-bri-demo", dst)


src = cv.imread("E:/cat.jpg")
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow("image", src)
contrast_brightness_image(src, 1.2, 10)  # 第一个1.2为对比度  第二个为亮度数值越大越亮
cv.waitKey(0)
cv.destroyAllWindows()