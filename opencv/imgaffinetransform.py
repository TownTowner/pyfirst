import cv2
import numpy as np


def flip():
    # Load the image and convert it to grayscale
    img = cv2.imread("./data/imgs/pixpin.png")
    # Flip the image vertically, horizontally
    img = cv2.flip(img, 1)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate():
    # Load the image and convert it to grayscale
    img = cv2.imread("./data/imgs/pixpin.png")
    print(f"before: {img.shape = }")
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    print(f"after: {img.shape = }")

    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def affine_transform():
    # Load the image and convert it to grayscale
    img = cv2.imread("./data/imgs/pixpin.png")
    cv2.imshow("Original", img)

    height, width = img.shape[:2]
    print(f"{height = }, {width = }")
    # Create a matrix to rotate the image by 90 degrees
    # M = np.float32([[1, 0, 200], [0, 1, 0]])  # 向右平移200像素
    M = np.float32([[1, 0, 200], [0, 1, 200]])  # 向右向下平移200像素
    # Apply the affine transformation to the image
    img = cv2.warpAffine(img, M, (width, height))
    cv2.imshow("Affine", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # flip()
    # rotate()
    affine_transform()
