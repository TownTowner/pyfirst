import numpy as np
import cv2


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def rotate_affine(image):
    (h, w) = image.shape[:2]

    src = np.float32([[0, 0], [w, 0], [0, h]])
    dst = np.float32([[0, h // 2], [w // 2, 0], [w // 2, h // 2]])
    M = cv2.getAffineTransform(src, dst)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def rotate_perspective(image):
    (h, w) = image.shape[:2]
    print(h, w)  # 580,1012

    # 1050,246
    # 1778,1008
    # 1050/1778*1012=597,150/1008*580=86 => 600,85
    # 784/1778*1012=446,736/1008*580=423 => 445,420
    # 1373/1778*1012=781,580             => 780,580
    # 1012,326/1008*580=188              => 1010,190
    src = np.float32([[605, 0], [1012, 150], [450, 405], [765, 580]])
    dst = np.float32([[0, 0], [407, 0], [0, 150], [407, 150]])
    # dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    M = cv2.getPerspectiveTransform(src, dst)
    rotated = cv2.warpPerspective(image, M, (410, 105))
    return rotated


if __name__ == "__main__":
    img = cv2.imread("./data/imgs/pixpin.png")
    # rotated = rotate(img, 45)
    # rotated = rotate_affine(img)
    rotated = rotate_perspective(img)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
