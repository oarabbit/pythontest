import cv2 as cv

src = cv.imread("E:\cat.jpg")
# 读图像
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# 通过opencv框架创建一个窗口
# 第二个参数不写或者WINDOW_AUTOSIZE：不可改变窗口大小
# 0或者cv.WINDOW_NORMAL：可以改变窗口大小
cv.imshow("input image",src)
# 在窗口中显示图像
# 第一个参数名称和namedWindow参数一样
# 如果是CV_WINDOW_AUTOSIZE（默认值），显示图像原始大小
# 否则，将图像进行缩放以适合窗口
cv.waitKey(0)
# 等待响应操作
#  k<=0:一直显示，键盘上按下一个数字键即会消失
#  k>0:这一帧显示多少毫秒，到下一帧

cv.destroyAllWindows()
print("Hi,Python!")