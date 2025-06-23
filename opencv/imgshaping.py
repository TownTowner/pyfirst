from cv2.typing import MatLike
import numpy as np
import cv2


def thresholdExec(img) -> (MatLike, MatLike):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 阈值分割,thresh为阈值，result为分割后的图像
    # 第一个参数是源图像，必须是灰度图。
    # 第二个参数是阈值，范围通常为0-255（8位图像），用于像素分类的临界值，示例：125表示像素值>125的会被设为maxval
    # 第三个参数是当像素值高于阈值时应该被赋予的新的像素值；当像素值超过阈值时赋予的新值， 二值化通常设为255（白色）， 其他场景可根据需要调整
    # 第四个参数是
    #   - cv2.THRESH_BINARY ：标准二值化
    #   - cv2.THRESH_BINARY_INV ：反向二值化
    #   - cv2.THRESH_MASK ：掩码
    #   - cv2.THRESH_OTSU ：大津法 # 必须与基础阈值类型组合使用
    #   - cv2.THRESH_TRIANGLE ：三角形法
    #   - cv2.THRESH_TOZERO ：低于阈值置零
    #   - cv2.THRESH_TOZERO_INV ：高于阈值置零
    #   - cv2.THRESH_TRUNC ：截断
    #   - 可组合使用自适应阈值：
    #       cv2.THRESH_BINARY + cv2.THRESH_OTSU
    #       cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE

    thresh, result = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
    return result, img


def adaptiveThresholdExec(img) -> (MatLike, MatLike):
    # 阈值分割,thresh为阈值，result为分割后的图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 自适应阈值分割,result为分割后的图像
    # 第一个参数是源图像，必须是灰度图。
    # 第二个参数是对像素值进行分类的阈值。
    # 第三个参数是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。
    # 第四个参数是一个确定如何计算阈值的方法。
    # 第五个参数是一个常数，它是从均值或加权均值中减去的。
    result = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 0
    )
    return result, img


def erodeExec(img) -> (MatLike, MatLike):
    # 腐蚀
    # kernel 或者 iterations 至少一个为真，否则返回原图
    # kernel 为卷积核，iterations 为腐蚀次数，可调试这2个参数，观察效果
    # kernel = np.ones((3, 3), np.uint8)

    # cv2.getStructuringElement() 函数用于获取指定形状和大小的结构元素
    # 第一个参数是结构元素的形状，有以下几种选择：
    #   - cv2.MORPH_RECT：矩形
    #   - cv2.MORPH_CROSS：交叉
    #   - cv2.MORPH_ELLIPSE：椭圆
    # 第二个参数是结构元素的大小，一般为一个元组，例如 (3, 3)
    # 第三个参数是锚点的位置，默认为 (-1, -1)，表示锚点在中心
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    result = cv2.erode(img, kernel, iterations=3)  # iterations为腐蚀次数
    return result, img


def dilateExec(img) -> (MatLike, MatLike):
    # 膨胀
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    result = cv2.dilate(img, kernel, iterations=3)
    return result, img


def openExec(img) -> (MatLike, MatLike):
    # 开运算 = 腐蚀 + 膨胀, 可去除噪声,
    # 开运算的作用是去除物体外部的噪声，同时保持物体的形状
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 原始操作
    # ero = cv2.erode(img, kernel, iterations=3)  # iterations为腐蚀次数
    # result = cv2.dilate(ero, kernel, iterations=3)
    # 直接调用
    result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=3)
    return result, img


def closeExec(img) -> (MatLike, MatLike):
    # 闭运算 = 膨胀 + 腐蚀, 可去除噪声
    # 闭运算的作用是填充物体内部的空洞，同时保持物体的形状
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 原始操作
    # dil = cv2.dilate(img, kernel, iterations=2)  # iterations为腐蚀次数
    # result = cv2.erode(dil, kernel, iterations=2)  # iterations为腐蚀次数
    # 直接调用
    result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)
    return result, img


def gradientExec(img) -> (MatLike, MatLike):
    # 梯度 = 膨胀 - 腐蚀, 可保留物体的边缘轮廓
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 原始操作
    # dil = cv2.dilate(img, kernel, iterations=1)
    # ero = cv2.erode(img, kernel, iterations=1)
    # result = cv2.subtract(dil, ero)  # 膨胀 - 腐蚀
    # 直接调用
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)
    return result, img


def tophatExec(img) -> (MatLike, MatLike):
    # 顶帽 = 原图 - 开运算, 可保留物体的外部轮廓
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 原始操作
    # open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    # result = cv2.subtract(img, open)  # 原图 - 开运算
    # 直接调用
    result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=1)
    return result, img


def blackhatExec(img) -> (MatLike, MatLike):
    # 黑帽 = 闭运算 - 原图, 可保留物体的内部轮廓
    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 原始操作
    # close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
    # result = cv2.subtract(close, img)  # 闭运算 - 原图
    # 直接调用
    result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=1)
    return result, img


def getImg(picName):
    path = f"./data/imgs/{picName}"
    img = cv2.imread(path)
    return (img, path)


def main():
    # 读取图像
    spong = "spongbob.png"
    pix = "pixpin.png"
    lena = "lena.png"
    tan = "tan.png"
    shudu = "shudu.png"
    mashibing = "mashibing.png"
    j = "j.png"
    j_dot = "j_dot.png"
    j_dot_inner = "j_dot_inner.png"
    # img = cv2.imread(f"./data/imgs/{mashibing}")

    # result,img = thresholdExec(getImg(spong)[0]) # 阈值分割
    # result,img = adaptiveThresholdExec(getImg(lena)[0])  # 自适应阈值分割s
    # result, img = erodeExec(getImg(mashibing)[0])  # 腐蚀
    # # result, img = dilateExec(result)  # 先腐蚀，再膨胀，可去除噪声

    # result, img = dilateExec(getImg(j)[0])  # 膨胀
    # result, img = openExec(getImg(j_dot)[0])  # 开运算
    # result, img = closeExec(getImg(j_dot_inner)[0])  # 闭运算
    # result, img = gradientExec(getImg(j)[0])  # 梯度
    # result, img = tophatExec(getImg(j_dot)[0])  # 顶帽
    result, img = blackhatExec(getImg(j_dot_inner)[0])  # 黑帽

    # theone = None
    # for img in [spong, pix, lena, shudu, tan, mashibing]:
    #     if np.array_equal(img.shape, result.shape):
    #         theone = img
    #         break
    # theone = np.hstack((theone, result)) if theone is not None else result

    cv2.imshow("result", np.hstack((img, result)))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
