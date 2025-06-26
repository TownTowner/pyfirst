import cv2
import numpy as np


def main():
    original = cv2.imread("./data/imgs/pixpin.png")
    colorTrans = [
        cv2.COLOR_BGR2BGRA,
        cv2.COLOR_BGR2GRAY,
        cv2.COLOR_BGR2HLS,
        cv2.COLOR_BGR2HSV,
        cv2.COLOR_BGR2YUV,
    ]
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Color", "image", 0, len(colorTrans) - 1, lambda x: x)
    while True:
        color = cv2.getTrackbarPos("Color", "image")
        img = cv2.cvtColor(original, colorTrans[color])
        cv2.imshow("image", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()


# im = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
# im[0:2, 0:2] = [1, -1]  # [1]
if __name__ == "__main__":
    main()
    # print(im)
