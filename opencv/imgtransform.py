import cv2
import numpy as np


def main():
    # Load the two images
    img1 = cv2.imread("./data/imgs/pixpin.png")
    img2 = cv2.imread("./data/imgs/tan.png")

    print(img1.shape)
    print(img2.shape)
    # Resize the images to the same size (optional)
    # img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    # 按比例縮小圖片，(default)INTER_LINEAR 是插值方法，cv2.INTER_LINEAR 是線性插值，
    # cv2.INTER_AREA 是區域插值, cv2.INTER_CUBIC 是三次插值, cv2.INTER_LANCZOS4 是Lanczos插值
    img2 = cv2.resize(img2, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    print("img1 resize:", img2.shape)

    cv2.imshow("img", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
