import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    # 形状第一维度
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s height : %s channels : %s"%(width, height, channels))
    for row in range(height):
    #从0开始
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                # 三维数组
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo",image)


print("---------Hello Python---------")
src = cv.imread("E:/cat.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1 = cv.getTickCount()
# 毫秒级别的计时函数,记录了系统启动以来的时间毫秒
access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
# getTickFrequency用于返回CPU的频率,就是每秒的计时周期数，毫秒的周期数要除以1000
print("time : %s ms"%(time * 1000))
# 运行时间(总次数/频率）
cv.waitKey(0)

cv.destroyAllWindows()