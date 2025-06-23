import cv2
import numpy as np


def main():
    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)

    img = np.zeros((480, 640, 3), np.uint8)
    # 3维数组，每个元素是一个点的坐标，每个点是一个二维数组，每个二维数组是一个点的坐标
    points = np.array([[[100, 100], [150, 50], [200, 100], [150, 150]]], np.int32)
    cv2.polylines(img, points, True, (0, 255, 0), 3)  # 绿色

    points = np.array([[[300, 100], [350, 50], [400, 100], [350, 150]]], np.int32)
    cv2.fillPoly(img, points, (255, 0, 0))  # 蓝色

    cv2.imshow("image", img)  # b,g 蓝绿合并的水蓝色
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
