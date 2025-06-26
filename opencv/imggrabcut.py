import cv2
import numpy as np


def main():
    img = cv2.imread("data/imgs/lena.png")
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (100, 100, 300, 300)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    # 0,2 -> bg, 1,3 -> fg
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
    # print(f"{mask.shape = }")
    # print(f"{mask = }")
    # print(f"{mask2.shape = }")
    # print(f"{mask2 = }")
    # print(f"{img.shape = }")
    # print(f"{img = }")
    img = img * mask2[:, :, np.newaxis]
    # print(f"{img.shape = }")
    # print(f"{img = }")
    

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
