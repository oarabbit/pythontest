import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("E:/WLOP Aeolian3 by Eliza Final.mp4")
    while True:
        ret,frame = capture.read()
        # 有的话返回真，没有的话返回假
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        # 转成hsv色彩空间
        # 设置颜色的范围，跟踪颜色
        lower_hsv = np.array([100,43,46])
        upper_hsv = np.array([124,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        # 调节图像颜色信息（H）、饱和度（S）、亮度（V）区间
        # 第一个参数是输入的图像，第二个参数是hsv三个通道的低值，第三个参数是高值
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitKey(40)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break


extrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()