import cv2
from cvzone.PoseModule import PoseDetector


def genPoseFile():
    cap = cv2.VideoCapture("data/videos/kun.mp4")
    detector = PoseDetector()
    positionList = []
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        img = detector.findPose(img)
        lmList, bbox = detector.findPosition(img, draw=False)
        if lmList:
            h = img.shape[0]
            # in unity x,y start from left-bottom, so we need to flip y
            lmStr = ",".join([f"{lm[0]},{h-lm[1]},{lm[2]}" for lm in lmList])
            positionList.append(lmStr)
            print(positionList)

        cv2.imshow("img", img)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    # with open("data/kun_motion.txt", "w") as f:
    #     f.write("\n".join(positionList))

    cap.release()
    cv2.destroyAllWindows()


def main():
    genPoseFile()


if __name__ == "__main__":
    main()
