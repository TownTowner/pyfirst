import cv2
import numpy as np


def main():
    img = cv2.imread("data/imgs/coin.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("img", img)

    # 二值化
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # cv2.imshow("thresh", thresh)

    # 形态学操作
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    # cv2.imshow("opening", opening)

    # # 找到图中的背景和前景
    # sure_bg = cv2.dilate(opening, kernel, iterations=3)
    # # cv2.imshow("sure_bg", sure_bg)
    # # 因为硬币之间彼此是接触的，导致腐蚀之后的前景图不太对，硬币和硬币之间形成了通道.
    # # 腐蚀在这里不适合.
    # sure_fg = cv2.erode(opening, kernel, iterations=3)
    # # cv2.imshow("sure_fg", sure_fg)
    # # 找到不确定的区域（硬币边界区域）
    # unknown = cv2.subtract(sure_bg, sure_fg)
    # # cv2.imshow("unknown", unknown)

    # 距离变换,distanceType计算距离的方式:DIST_L1,DIST_L2
    # maskSize:进行扫描时的kernel的大小，L1用3，L2用5
    dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    # 对dist进行归一化
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    print(dist.max())
    # cv2.imshow("dist", dist)

    # 距离变换后，对图像进行阈值处理，超过0.7的设置为前景，否则设置为背景
    ret, sure_fg = cv2.threshold(dist, 0.7 * dist.max(), 255, cv2.THRESH_BINARY)
    # 对sure_fg进行膨胀，得到确定的前景区域
    sure_fg = cv2.dilate(sure_fg, kernel, iterations=3)
    # 确定背景区域
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    sure_fg = sure_fg.astype("uint8")
    # print(f"{sure_bg = }")
    # print(f"{sure_fg = }")
    # 不确定区域
    unknown = cv2.subtract(sure_bg, sure_fg)
    # 标记前景区域和背景区域
    # cv2.imshow("bg", np.hstack((sure_bg, sure_fg, unknown)))

    # 连通区域标记
    ret, markers = cv2.connectedComponents(sure_fg)
    print(f"{markers.min() = },{ markers.max() = }")
    print(f"{ markers = }")
    # 确保背景区域为1，其他区域从2开始,
    # 因为watershed中 0 认为是不确定区域，1 是背景，大于 1 的是前景
    # markers＋1 把原来的 0 变成 1 了.
    markers = markers + 1
    # 标记不确定区域为0
    markers[unknown == 255] = 0

    # 进行分水岭算法,将边界区域标记为-1
    markers = cv2.watershed(img, markers)
    print(f"{markers.min() = },{ markers.max() = }")
    # markers = markers.astype("uint8")
    # cv2.imshow("markers", markers)

    # 标记边界
    # img[markers == -1] = [0, 0, 255]
    # 可筛选出前景
    # img[markers > 1] = [0, 255, 0]
    # cv2.imshow("watershed", img)

    # 抠出硬币
    # 先创建一个掩膜，大小和图像相同，背景为0，前景为1
    # print(img)
    # print(markers)
    mask = np.zeros_like(img, shape=img.shape[:2])
    # 把前景区域设置为255，其他位置（背景）赋值为0
    mask[markers > 1] = 255
    # print(mask.shape)
    # print(img.shape)

    # 对原图像进行掩膜操作
    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("res", res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
