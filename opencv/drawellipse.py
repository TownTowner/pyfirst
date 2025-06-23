import cv2
import numpy as np


def main():
    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)

    img = np.zeros((480, 640, 3), np.uint8)
    # 椭圆：      图像, 中心点, 长轴和短轴, 旋转角度, 起始角度, 终止角度, 颜色, 线宽
    cv2.ellipse(img, (100, 240), (100, 50), 0, 0, 180, (255, 0, 0), 5)
    cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 360, (255, 0, 0), 5)
    cv2.ellipse(img, (500, 240), (100, 50), 60, 0, 360, (255, 0, 0), 5)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
