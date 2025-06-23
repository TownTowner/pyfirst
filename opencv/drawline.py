import cv2
import numpy as np


def main():
    cv2.namedWindow("image")

    img = np.zeros((480, 640, 3), np.uint8)
    cv2.line(img, (0, 0), (640, 480), (255, 0, 0), 10)  # 蓝色
    cv2.line(img, (0, 480), (640, 0), (0, 255, 0), 10)  # 绿色
    cv2.line(img, (320, 0), (320, 480), (0, 0, 255), 10)  # 红色
    cv2.line(img, (0, 240), (640, 240), (0, 255, 255), 10)  # 黄色
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
