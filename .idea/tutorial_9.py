import cv2 as cv


# 逻辑运算：与或非的操作
def logic_image(src1, src2):
    # 与 两张图片同一位置的色素两个值均不为零的才会有输出
    src = cv.bitwise_and(src1, src2)
    cv.imshow("and", src)
    # 或 两张图片同一位置的色素两个值不全为零的会有输出
    src = cv.bitwise_or(src1, src2)
    cv.imshow("or", src)
    # 非 对一张图片操作  取反
    src = cv.bitwise_not(src1)
    cv.imshow("not", src)
    # 异或 两张图片同一位置的色素两个值有一个为零，另一个不为零才会输出
    src = cv.bitwise_xor(src1, src2)
    cv.imshow("xor", src)


src1 = cv.imread("E:/pic01.jpg")
src2 = cv.imread("E:/pic02.jpg")
cv.imshow("image1", src1)
cv.imshow("image2", src2)
logic_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()