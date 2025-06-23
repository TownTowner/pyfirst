from cProfile import label
import cv2
import numpy as np
from cv2.typing import MatLike
from matplotlib import pyplot as plt


def calcuHistExec(img) -> (MatLike, MatLike):
    # 直方图计算
    # 直方图是一种用于表示图像中像素分布的图形工具。
    # 它可以帮助我们了解图像的亮度、对比度、颜色分布等信息。
    # 直方图的计算通常包括以下几个步骤：
    # 1. 图像灰度化：将彩色图像转换为灰度图像。
    # 2. 直方图计算：对灰度图像进行直方图计算。
    # 3. 直方图显示：将直方图显示出来。
    # 4. 直方图比较：比较两个图像的直方图。
    # 5. 直方图均衡化：对图像进行直方图均衡化。
    # 6. 直方图反向投影：将直方图应用到另一个图像上。

    # 绘制直方图,use plt to show histogram
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # plt.hist(gray.ravel(), 256, [0, 255])
    # plt.show()

    # 计算直方图，返回一个数组，数组的长度为256，数组的每个元素表示对应灰度级别的像素个数。
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    histg = cv2.calcHist([img], [1], None, [256], [0, 255])
    histr = cv2.calcHist([img], [2], None, [256], [0, 255])
    plt.plot(histb, color="b")  # 蓝色
    plt.plot(histg, color="g")  # 绿色
    plt.plot(histr, color="r")  # 红色
    plt.show()
    # print(f"{hist = }")
    return histb, img


def equalizeHistExec(img):
    # 直方图均衡化，用于增强图像的对比度，使图像更加清晰。
    # 直方图均衡化的步骤如下：
    # 1. 图像灰度化：将彩色图像转换为灰度图像。
    # 2. 直方图均衡化：对灰度图像进行直方图均衡化。
    # 3. 直方图显示：将直方图显示出来。
    # 4. 直方图比较：比较两个图像的直方图。
    # 5. 直方图反向投影：将直方图应用到另一个图像上。
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 变黑
    gray_dark = gray - 40
    # 变亮
    gray_light = gray + 40

    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 255])
    dark_hist = cv2.calcHist([gray_dark], [0], None, [256], [0, 255])
    light_hist = cv2.calcHist([gray_light], [0], None, [256], [0, 255])
    plt.plot(gray_hist, label="gray")
    plt.plot(dark_hist, label="dark")
    plt.plot(light_hist, label="light")
    plt.legend()
    plt.show()

    dark_equ = cv2.equalizeHist(gray_dark)
    light_equ = cv2.equalizeHist(gray_light)
    # plt.plot(dark_equ, label="dark_equ")
    # plt.plot(light_equ, label="light_equ")
    # plt.legend()
    # plt.show()

    dark_equ_hist = cv2.calcHist([dark_equ], [0], None, [256], [0, 255])
    light_equ_hist = cv2.calcHist([light_equ], [0], None, [256], [0, 255])
    # plt.plot(gray, label="gray")
    plt.plot(dark_equ_hist, label="dark_equ_hist")
    plt.plot(light_equ_hist, label="light_equ_hist")
    plt.legend()
    plt.show()

    res = np.hstack((gray, gray_dark, gray_light, dark_equ, light_equ))
    return res, img


def maskExec(img):
    # 直方图掩码
    # 直方图掩码是一种用于增强图像对比度的方法。
    # 直方图掩码的步骤如下：
    # 1. 图像灰度化：将彩色图像转换为灰度图像。
    # 2. 直方图掩码：对灰度图像进行直方图掩码。
    # 3. 直方图显示：将直方图显示出来。
    # 4. 直方图比较：比较两个图像的直方图。
    # 5. 直方图反向投影：将直方图应用到另一个图像上。
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.zeros(gray.shape, np.uint8)
    mask[100:300, 100:400] = 255
    masked_img = cv2.bitwise_and(gray, gray, mask=mask)
    return masked_img, img


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

    # result, img = calcuHistExec(getImg(lena)[0])  # 直方图计算
    # result, img = equalizeHistExec(getImg(lena)[0])  # 直方图均衡化
    result, img = maskExec(getImg(lena)[0])  # 直方图掩码

    cv2.imshow("img", img)
    cv2.imshow("result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
