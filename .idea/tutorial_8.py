import cv2 as cv


# 数值运算：加减乘除
def shu_image(src11, src22):
    src = cv.add(src11, src22)
    # 加：黑色的值为0，超过255默认255，所以是叠加
    cv.imshow("相加", src)
    src = cv.subtract(src11, src22)
    # 减：小于0 默认为0
    cv.imshow("相减", src)
    src = cv.divide(src11, src22)
    # 乘
    cv.imshow("相乘", src)
    src = cv.multiply(src11, src22)
    # 除
    cv.imshow("相除", src)

src1 = cv.imread("E:\pic01.jpg")
src2 = cv.imread("E:\pic02.jpg")
cv.imshow("image1", src1)
cv.imshow("image2", src2)
shu_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()