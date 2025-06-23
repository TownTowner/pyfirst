import cv2
import numpy as np
from cv2.typing import MatLike


def gaussianPyramidExec(img) -> (MatLike, MatLike):
    # 高斯金字塔
    # 这些图像是通过对原始图像进行高斯模糊来得到的。
    # 高斯金字塔的每个图像都是通过对前一个图像进行高斯模糊来得到的。
    result = cv2.pyrDown(img)  # 下采样
    return result, img


def gaussianPyramidUpExec(img) -> (MatLike, MatLike):
    # 高斯金字塔
    # 这些图像是通过对原始图像进行高斯模糊来得到的。
    # 高斯金字塔的每个图像都是通过对前一个图像进行高斯模糊来得到的。
    result = cv2.pyrUp(img)  # 下采样
    return result, img


def laplacianPyramidExec(img) -> (MatLike, MatLike):
    # 拉普拉斯金字塔 = 原始图像 - 上采样(下采样图像)
    # 拉普拉斯金字塔的每个图像都是通过对前一个图像进行高斯模糊和下采样来得到的。
    # 原始操作
    gaussian = cv2.pyrDown(img)  # 下采样
    gaussianUp = cv2.pyrUp(gaussian)  # 上采样

    result = cv2.subtract(img, gaussianUp)  # 原始图像 - 上采样图像

    cv2.imshow("result1", result.copy())
    # 第二层拉普拉斯金字塔
    gaussian2 = cv2.pyrDown(gaussianUp)  # 下采样
    gaussianUp2 = cv2.pyrUp(gaussian2)  # 上采样
    result = cv2.subtract(gaussianUp, gaussianUp2)  # 原始图像 - 上采样图像
    return result, img


def getImg(picName):
    path = f"./data/imgs/{picName}"
    img = cv2.imread(path)
    return (img, path)  # 返回图像和路径，方便后续使用，如显示图像、保存图像等操作。


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
    contour1 = "contour1.png"
    hand = "hand.png"
    hello = "hello.png"

    # result, img = gaussianPyramidExec(getImg(lena)[0])  # 高斯金字塔
    # result, img = gaussianPyramidUpExec(getImg(lena)[0])  # 高斯金字塔
    result, img = laplacianPyramidExec(getImg(lena)[0])  # 拉普拉斯金字塔

    cv2.imshow("img", img)
    cv2.imshow("result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
