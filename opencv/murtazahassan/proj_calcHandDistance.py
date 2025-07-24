from turtle import distance
import cv2
import numpy as np
import detectorModules as dm


# 定义一个函数，用于计算距离
def calcDistance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    # fmt:off
    xSimple = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
    # fmt:on
    ySimple = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    coff = np.polyfit(xSimple, ySimple, 2)  # y = Ax^2 + Bx + C
    a, b, c = coff

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    detector = dm.HandDetector()
    handNo = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        detector.detect(img)
        handsDict = detector.drawAndFindPosition(img, handNo=handNo)
        hand = handsDict[handNo] if len(handsDict) != 0 else None
        if hand is not None:
            lmList = hand["lms"]
            x, y, w, h = hand["bbox"]
            distance = calcDistance(
                lmList[5][0], lmList[5][1], lmList[17][0], lmList[17][1]
            )
            distanceCM = a * distance**2 + b * distance + c
            # print(distanceCM, distance)
            txt = f"{distanceCM:.2f} cm"
            cv2.putText(img, txt, (x, y - 30), fnt, 2, (255, 0, 0), 2)

        cv2.imshow("img", img)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
