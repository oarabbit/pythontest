import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    # 打开第0个相机
    while(True):
        ret,frame = capture.read
        # 进行读写操作，返回两个参数
        # 第一个参数是bool型的ret，其值为True或False，代表有没有读到图片
        # 第二个参数是frame，是当前截取一帧的图片
        frame = cv.flip(frame,1)
        # 镜像变换
        # 0为上下颠倒，大于0为水平颠倒，小于0为180旋转
        cv.imshow("video",frame)
        # 每一帧循环显示
        c = cv.waitKey(50)
        # 延迟50ms
        if c == 27:
            break
        # esc关闭
        # if cv.waitKey(10) & 0xFF == ord('q'):
        # 键盘输入q退出窗口，不按q点击关闭会一直关不掉，也可以设置成其他键。
            break

def get_image_info(image):
# 定义函数
    print(type(image))
    # 类别，显示图片类型 numpy类型的数组
    print(image.shape)
    # 图像矩阵的shape属性表示图像的形状，shape会返回tuple元组
    # 第一个元素表示矩阵行数（高）
    # 第二个元组表示矩阵列数（宽）
    # 第三个元素是3（像素点通道数），表示像素值由光的三原色组成
    print(image.size)
    # 大小
    print(image.dtype)
    # 每个通道所占的位数
    pixel_data = np.array(image)
    # 获取所有的像素数据（图片矩阵）
    print(pixel_data)


print("---------Hello Python---------")
src = cv.imread("E:/cat.jpg")
cv.namedWindow("put image",cv.WINDOW_AUTOSIZE)
cv.imshow("put image",src)
get_image_info(src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# 变成灰度图像
cv.imwrite("D:/result.png",gray)
# 保存
cv.waitKey(0)

cv.destroyAllWindows()
# 删除窗口