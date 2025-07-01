from PIL import Image
from cv2.typing import MatLike
import cv2
import numpy as np
import pytesseract


def standardize(img, width=None, height=500):
    if width is None and height is None:
        return img
    if width is None:
        width = int(img.shape[1] * height / img.shape[0])
    if height is None:
        height = int(img.shape[0] * width / img.shape[1])
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)


def order_points(pts):
    # 初始化坐标点
    rect = np.zeros((4, 2), dtype="float32")
    # 按照左上、右上、右下、左下的顺序对坐标点进行排序
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


def four_point_transform(image, pts) -> MatLike:
    # 获取坐标点
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # 计算新图像的宽度
    widthT = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthT), int(widthB))
    # 计算新图像的高度
    heightR = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightL = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightR), int(heightL))
    # 变换矩阵
    dst = np.array(
        [[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]],
        dtype="float32",
    )
    M = cv2.getPerspectiveTransform(rect, dst)
    # 变换
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def get_border(img) -> MatLike:
    contours, hierarchy = cv2.findContours(
        img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
    )
    # 轮廓排序
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # 找到最大轮廓
    for c in contours:
        # 计算周长
        peri = cv2.arcLength(c, True)
        # 多边形逼近
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break
    return screenCnt


def main():
    pic_name = "recepit"
    # pic_name = "rim"
    pic_name = "page"
    pic_ext = ".jpg"
    base_path = "data/imgs/"
    img = cv2.imread(f"{base_path}{pic_name}{pic_ext}")
    ratio = img.shape[0] / 500.0
    resized = standardize(img.copy())

    print(f"{ratio = }")
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # 高斯化
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # 边缘检测
    edges = cv2.Canny(gray, 75, 200)
    # ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    screenCnt = get_border(edges)
    cv2.drawContours(resized, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("resized", resized)

    # 抠图变换
    warped = four_point_transform(img, screenCnt.reshape(4, 2) * ratio)
    print(f"{warped.shape= }")
    # cv2.imshow("warped1", warped)
    # 二值化
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("warpedgray", warped)

    _, thresh = cv2.threshold(warped, 150, 255, cv2.THRESH_BINARY)
    # 显示
    cv2.imshow("warped", thresh)

    # 保存起来
    save_path = f"{base_path}{pic_name}_thresh{pic_ext}"
    cv2.imwrite(save_path, thresh)
    result = pytesseract.image_to_string(Image.open(save_path))
    print(result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
