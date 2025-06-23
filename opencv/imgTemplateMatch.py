import numpy as np
import cv2


def main():
    lena = cv2.imread("data/imgs/lena.png")
    template = cv2.imread("data/imgs/lena_face.png")
    h, w, _ = template.shape
    lena_gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(lena_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    # print(res)

    # 1. use minMaxLoc to find the max value and min value
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(f"{min_val = }, {max_val = }, {min_loc = }, {max_loc = }")
    # !important TM_SQDIFF 越小越好，TM_CCOEFF、TM_CCORR越大越好
    # 1.1 use cv2.matchTemplate(..., cv2.TM_CCOEFF_NORMED)
    max_pt1, max_pt2 = max_loc, (max_loc[0] + w, max_loc[1] + h)
    lena = cv2.rectangle(lena, max_pt1, max_pt2, (0, 0, 255), 2)
    # 1.2 use cv2.matchTemplate(..,cv2.TM_SQDIFF)
    # min_pt1, min_pt2 = min_loc, (min_loc[0] + w, min_loc[1] + h)
    # lena = cv2.rectangle(lena, min_pt1, min_pt2, (0, 0, 255), 2)

    # 2. use threshold to find the location
    # threshold = 0.8
    # loc = np.where(res >= threshold)
    # print(loc)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(lena, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imshow("lena", lena)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
