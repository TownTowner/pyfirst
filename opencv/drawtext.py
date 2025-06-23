import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def main():
    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)

    img = np.zeros((480, 640, 3), np.uint8)
    cv2.putText(
        img, "Hello World你好", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3
    )
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
