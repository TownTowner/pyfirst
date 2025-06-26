import cv2
import numpy as np


def callback(x):
    print(x)


def main():
    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)
    cv2.createTrackbar("R", "image", 0, 255, callback)
    cv2.createTrackbar("G", "image", 0, 255, callback)
    cv2.createTrackbar("B", "image", 0, 255, callback)

    img = np.zeros((480, 640, 3), np.uint8)
    while True:
        r = cv2.getTrackbarPos("R", "image")
        g = cv2.getTrackbarPos("G", "image")
        b = cv2.getTrackbarPos("B", "image")
        img[:] = [b, g, r]
        cv2.imshow("image", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
