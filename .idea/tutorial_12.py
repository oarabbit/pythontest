import cv2 as cv
import numpy as np


# 指定颜色替换
def fill_color_demo(image):
    # 复制原图像
    copyImage = image.copy()
    # 读取图像的宽和高
    h, w = image.shape[:2]
    # 新建图像矩阵  +2是官方函数要求
    mask = np.zeros([h + 2, w + 2], np.uint8)
    # floodFill( 1.操作的图像, 2.掩模, 3.起始像素值，4.填充的颜色（新的值）, 5.填充颜色的低值， 6.填充颜色的高值 ,7.填充的方法)
    # 先在（30,30）减去这个低值，加上高值，符合这个范围的进行填充
    cv.floodFill(copyImage, mask, (0, 80), (0, 100, 255), (100, 100, 50), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImage)


src = cv.imread("E:/cat.jpg")
cv.imshow("image", src)
fill_color_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()