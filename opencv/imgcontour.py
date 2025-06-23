import cv2
import numpy as np
from cv2.typing import MatLike


def findContourExec(img) -> (MatLike, MatLike):
    # 轮廓检测
    # 轮廓检测是一种基于图像边缘的方法，用于发现图像中的物体轮廓。
    # 它可以用于图像分割、物体识别、形状分析等应用。
    # 轮廓检测的基本步骤如下：
    # 1. 图像预处理：对输入图像进行预处理，包括灰度化、二值化、去噪等操作，以提高轮廓检测的效果。
    # 2. 边缘检测：使用边缘检测算法（如Canny边缘检测）来检测图像中的边缘。
    # 3. 轮廓提取：根据边缘信息，提取图像中的轮廓。
    # 4. 轮廓绘制：将提取的轮廓绘制到原始图像上，以便可视化和分析。
    # 5. 轮廓分析：对提取的轮廓进行分析，如计算轮廓的面积、周长、质心等特征。
    # 6. 轮廓筛选：根据需求，对提取的轮廓进行筛选，如根据面积、周长等特征进行筛选。
    # 7. 轮廓跟踪：对提取的轮廓进行跟踪，以便实现物体的跟踪和运动分析。
    # 8. 轮廓匹配：将提取的轮廓与已知的轮廓进行匹配，以便实现物体的识别和分类。
    # 9. 轮廓分割：将提取的轮廓进行分割，以便实现物体的分割和提取。
    # 10. 轮廓融合：将提取的轮廓进行融合，以便实现物体的融合和合成。
    # 11. 轮廓优化：对提取的轮廓进行优化，以便实现物体的优化和改进。
    # 12. 轮廓可视化：将提取的轮廓进行可视化，以便实现物体的可视化和展示。
    # 13. 轮廓应用：将提取的轮廓应用于实际应用中，如机器人导航、智能视觉等。
    # 14. 轮廓评估：对提取的轮廓进行评估，以便实现物体的评估和改进。
    # 15. 轮廓总结：对提取的轮廓进行总结，以便实现物体的总结和分析。
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 二值化

    # 轮廓检测
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    # 绘制轮廓，-1表示绘制所有轮廓，(0, 0, 255)表示轮廓颜色，3表示轮廓线条宽度
    result = img.copy()
    cv2.drawContours(result, contours, -1, (0, 0, 255), 2)

    area = cv2.contourArea(contours[0])  # 计算轮廓面积
    print(f"{area = }")
    perimeter = cv2.arcLength(contours[0], True)  # 计算轮廓周长
    print(f"{perimeter = }")

    return result, img, contours, hierarchy, area, perimeter


def approxPolyExec(img) -> (MatLike, MatLike):
    result, img, contours, hierarchy, area, perimeter = findContourExec(img)  # 轮廓检测
    # 多边形逼近
    approx = cv2.approxPolyDP(contours[0], 0.02 * perimeter, True)  #
    # print(f"{type(approx) = }")  # ndarray
    cv2.drawContours(result, [approx], 0, (0, 255, 0), 2)

    # 绘制轮廓
    return result, img, contours, hierarchy, area, perimeter


def convexHullExec(img) -> (MatLike, MatLike):
    result, img, contours, *_ = findContourExec(img)  # 轮廓检测
    # 凸包
    hull = cv2.convexHull(contours[0])  # 计算凸包
    cv2.drawContours(result, [hull], 0, (0, 255, 0), 2)  # 绘制凸包
    return result, img


def minAreaRectExec(img) -> (MatLike, MatLike):
    result, img, contours, hierarchy, area, perimeter = findContourExec(img)  # 轮廓检测
    # 绘制多边形, 1表示绘制第1个轮廓
    # cv2.drawContours(result, contours, 1, (0, 255, 0), 2)

    # 最小外接矩形,rect为RotatedRect旋转的矩形，包括(矩形的起始坐标(x，y)，矩形的长宽(w,h)，矩形旋转角度)
    rect = cv2.minAreaRect(contours[1])  # 计算最小外接矩形, 1表示绘制第1个轮廓
    # print(f"{rect = }")  # 输出最小外接矩形的四个顶点的坐标,

    # box为最小外接矩形的四个顶点的坐标
    box = np.round(cv2.boxPoints(rect)).astype(np.int32)  # 计算最小外接矩形的四个顶点
    print(f"{box = }")  # 输出最小外接矩形的四个顶点的坐标, 类型为ndarray
    cv2.drawContours(result, [box], 0, (255, 0, 0), 2)  # 绘制最小外接矩形
    return result, img


def boundingRectExec(img) -> (MatLike, MatLike):
    result, img, contours, *_ = findContourExec(img)  # 轮廓检测
    # 绘制多边形, 1表示绘制第1个轮廓
    # cv2.drawContours(result, contours, 1, (0, 255, 0), 2)
    # 最大外接矩形,rect为RotatedRect旋转的矩形，包括(矩形的起始坐标(x，y)，矩形的长宽(w,h)，矩形旋转角度)
    rect = cv2.boundingRect(contours[1])  # 计算最大外接矩形, 1表示绘制第1个轮廓
    print(f"{rect = }")  # 输出最大外接矩形的四个顶点的坐标, 类型为ndarray
    cv2.rectangle(result, rect, (255, 0, 0), 2)  # 绘制最大外接矩形
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

    # result, img = findContourExec(getImg(contour1)[0]) # 轮廓检测
    # result, img = approxPolyExec(getImg(hand)[0])  # 多边形逼近
    # result, img = convexHullExec(getImg(hand)[0])  # 凸包
    # result, img = minAreaRectExec(getImg(hello)[0])  # 最小外接矩形
    result, img = boundingRectExec(getImg(hello)[0])  # 最大外接矩形

    cv2.imshow("result", np.hstack((img, result)))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
