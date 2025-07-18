import cv2
import time
import os
import detectorModules as dm


def loadFingerImgs():
    path = "data/imgs/fingers/"
    images = []
    for img in os.listdir(path):
        curImg = cv2.imread(f"{path}/{img}")
        images.append(curImg)
    return images


def main():
    fingerImgs = loadFingerImgs()
    detector = dm.HandDetector()

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 70)
    handNo = 0  # hand number
    # [4, 8, 12, 16, 20]  # thumb, index, middle, ring, pinky
    thumbId = 4
    tipIds = [8, 12, 16, 20]
    fnt = cv2.FONT_HERSHEY_PLAIN
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        results = detector.detect(img)
        lmDict = detector.drawAndFindPosition(img, results, handNo, draw=False)
        handLm = lmDict.get(handNo, {})
        lmList = handLm.get("lms", [])
        if len(lmList) != 0:
            # print(lmList[4])
            fingerHits = []

            # left hand
            thumbHit = 1 if lmList[thumbId][0] < lmList[thumbId - 1][0] else 0
            # right hand
            thumbHit = 1 if lmList[thumbId][0] > lmList[thumbId - 1][0] else 0
            fingerHits.append(thumbHit)
            for tipId in tipIds:
                finHit = 1 if lmList[tipId][1] < lmList[tipId - 2][1] else 0
                fingerHits.append(finHit)

            print(fingerHits)

            fingetCount = fingerHits.count(1)
            finger = fingerImgs[fingetCount - 1]
            h, w, c = finger.shape
            img[0:h, 0:w] = finger

            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f"{fingetCount}", (40, 375), fnt, 10, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
