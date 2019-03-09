import cv2 as cv
import numpy as np


def create_image():
    '''
    img = np.zeros([400, 400, 3], np.uint8)
    #zeros:double类零矩阵，创建400*400大小、3个通道的矩阵图像，参数classname为uint8
    img[:, :, 0] = np.ones([400, 400])*255
    # 改变第0个通道的值，ones([400,400])：创建一个400*400的全1矩阵，*255：全255矩阵
    img[:, :, 1] = np.ones([400, 400])*255
    # 改变第二个通道的值
    img[:, :, 2] = np.ones([400, 400])*255
    # 改变第三个通道的值
    cv.imshow("new image1", img)
    # 输出一张400*400的白色图片(255 255 255):蓝(B)、绿(G)、红(R)

    img = np.ones([400, 400, 3], np.uint8)
    img[:, :, 0] = img[:, :, 0]*255
    img[:, :, 1] = img[:, :, 1]*255
    img[:, :, 2] = img[:, :, 2]*255
    cv.imshow("new image2", img)
    # 单独使用ones函数

    img = np.ones([400, 400, 1], np.uint8)
    # 单通道
    img = img * 0
    cv.imshow("new image2", img)
    '''

    m1 = np.ones([3,3],np.float32)
    # 尽量用浮点数或整形
    m1.fill(122.388)
    # 对里面每个值填上122.388
    print(m1)

    m2 = m1.reshape([1,9])
    # 1行9列
    print(m2)

    m3 = np.array([[2,3,4],[4,5,6],[7,8,9]],np.int32)
    # [[2,3,4]
    #  [4,5,6]
    #  [7,8,9]]
    m3.fill(9)
    # [[9,9,9]
    #  [9,9,9]
    #  [9,9,9]]
    print(m3)


create_image()
cv.waitKey(0)
cv.destroyAllWindows()