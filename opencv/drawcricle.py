import cv2
import numpy as np


def main():
    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)

    img = np.zeros((480, 640, 3), np.uint8)
    cv2.circle(img, (320, 240), 100, (0, 0, 255), 10)  # 蓝色
    cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
