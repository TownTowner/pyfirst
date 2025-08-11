from unittest import result
import numpy as np
import cv2


def filter2D(img):
    # 定义卷积核,必须float类型
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # kernel = np.ones((5, 5), np.float32) / 25

    # 尝试其他卷积核
    # &. 突出轮廓
    # kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    # &. 浮雕效果
    # kernel = np.array([[-2, 1, 0], [-1, 1, 1], [0, 1, 2]])
    # &. 锐化
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # 对图像进行卷积操作
    result = cv2.filter2D(img, -1, kernel)
    return result


def boxfilter(img):
    # 不用手动创建卷积核，直接使用boxFilter函数
    # 第一个参数是输入图像，第二个参数是输出图像的深度，-1表示与输入图像相同
    # 第三个参数是卷积核的大小，第四个参数是是否进行归一化，True表示进行归一化
    result = cv2.boxFilter(img, -1, (5, 5), normalize=True)
    return result


def blurfilter(img):
    result = cv2.blur(img, (5, 5))
    return result


def gaussianfilter(img):
    result = cv2.GaussianBlur(img, (5, 5), sigmaX=1)
    return result


def medianfilter(img):
    result = cv2.medianBlur(img, 5)
    return result


def bilateralfilter(img):
    result = cv2.bilateralFilter(img, 7, 20, 50)
    return result


def main():
    # 读取图像
    # img = cv2.imread("./data/imgs/spongbob.png")
    img = cv2.imread("./data/imgs/lena.png")
    # cv2.imshow("original", img)

    # result = filter2D(img) # 卷积滤波
    # result = boxfilter(img)  # 方盒滤波
    # result = blurfilter(img)  # 均值滤波
    # result = gaussianfilter(img)  # 高斯滤波
    # result = medianfilter(img)  # 中值滤波
    result = bilateralfilter(img)  # 双边滤波

    # 显示结果
    cv2.imshow("result", np.hstack((img, result)))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
