import cv2
import time
import detectorModules as dm


def main():
    detector = dm.HandDetector()
    cap = cv2.VideoCapture(0)

    pTime = 0
    cTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        detector.detectAndDraw(frame)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10, 70), fnt, 3, (255, 0, 255), 3)

        cv2.imshow("frame", frame)
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
