import cv2
import numpy as np


def main():
    cv2.namedWindow("image")
    # cv2.resizeWindow("image", 640, 480)

    img = np.zeros((200, 200, 3), np.uint8)
    b, g, r = cv2.split(img)
    # cv2.imshow("image", np.hstack((b, g, r)))
    b[10:100, 10:100] = 255  # 10:100 是高度 10:100 是宽度
    g[10:100, 10:100] = 255
    img = cv2.merge((b, g, r))
    cv2.imshow("image", img)  # b,g 蓝绿合并的水蓝色
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
