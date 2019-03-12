import cv2 as cv
import numpy as np


def image(image):
    #均值模糊
    dst = cv.blur(image, (1, 3))
    cv.imshow("blur_demo", dst)

    # 中值模糊
    dst1 = cv.medianBlur(image, 5)
    cv.imshow("medianBlur_demo", dst1)

    # 高斯模糊
    # 前面设置值后面的值不会影响
    dst2 = cv.GaussianBlur(image, (5, 5), 2)
    cv.imshow("GaussianBlur_demo", dst2)

    # 双边滤波
    # d：邻域直径
    # 如果d有赋值，那么通过sigmaColor和d求sigmaSpace，反之也成立
    # sigmaColor：颜色标准差
    # sigmaSpace：空间标准差，尽量取小以免计算量大
    dst3 = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst3)


def custom_blur_demo(src):
    # 25*255会溢出，所有要除以25
    # 自定义矩阵
    kernel1 = np.ones((5, 5), np.float)/25
    # 使用的函数为：filter2D()：定义为filter2D(src,ddepth,kernel)
    # ddepth：深度，输入值为-1时，目标图像和原图像深度保持一致
    # kernel: 卷积核（或者是相关核）,一个单通道浮点型矩阵
    dst = cv.filter2D(src, -1, kernel1)
    cv.imshow("custom_blur_demo", dst)
    # 锐化，总和为0：边缘梯度，总和为1：增强
    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst2 = cv.filter2D(src, -1, kernel2)
    cv.imshow("custom_blur_demo2", dst2)


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


# 高斯噪声
# 高斯模糊对高斯噪声有抑制作用
def gussian_noise(image):
    h,w,c = image.shape
    # 每一行每一列都加上一个随机数
    for row in range(h):
        for col in range(w):
            # 0为矩阵中所有随机数的平均值
            # 20为标准差，3为size
            s = np.random.normal(0,20,3)
            # blue
            b = image[row, col, 0]
            # green
            g = image[row, col, 1]
            # red
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image",image)


# 均值迁移
# 可能会过度模糊，要加强边缘，类似油画的效果
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift_demo",dst)


src = cv.imread("E:/cat.jpg")
cv.namedWindow("input image", cv.WINDOW_NORMAL)
cv.imshow("input image", src)
image(src)
custom_blur_demo(src)
gussian_noise(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()