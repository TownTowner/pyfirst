import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    img = np.zeros((512, 512, 3), np.uint8)
    # 1. use cv2
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # BGR
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))

    cv2.putText(
        img, "OpenCV", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2
    )

    plt.imshow(img[:, :, ::-1])
    plt.show()


if __name__ == "__main__":
    main()
