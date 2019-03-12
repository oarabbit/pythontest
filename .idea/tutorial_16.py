import cv2 as cv
import numpy as np


# 模版匹配
def template_image():
    tpl = cv.imread("E:/test.jpg")
    target = cv.imread("E:/Eurus.jpg")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    # 方法：平方差，亮度，相关性
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        # 右下角
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("match" + np.str(md), target)


template_image()
cv.waitKey(0)
cv.destroyAllWindows()