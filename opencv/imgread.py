import numpy as np
import matplotlib.pyplot as plt
import cv2


def main():
    # 0: gray, 1: color, -1: unchanged(alpha channel)
    img = cv2.imread("data/imgs/pixpin.png", 0)
    # 1. use cv2
    # cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 2. use matplotlib
    # 在OpenCV中，图像默认以BGR格式存储，而matplotlib期望RGB格式。img[:, :, ::-1]这个操作将颜色通道从BGR转换为RGB，以便正确显示图像。
    # use cv2.cvtColor(img,cv2.COLOR_BGR2RGB) or img[:, :, ::-1]
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img[:, :, ::-1])
    plt.imshow(img, cmap=plt.cm.gray)  # when use cv2.imread("path.to.img",0)
    cv2.imwrite("data/imgs/pixpin_gray.png", img)
    plt.show()


if __name__ == "__main__":
    main()
