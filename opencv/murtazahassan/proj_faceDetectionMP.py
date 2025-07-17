import cv2
import time
from detectorModules import FaceDetector


def main():
    prevTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    cap = cv2.VideoCapture("data/videos/face1.mp4")
    faser = FaceDetector(fnt)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        faser.detectAndDraw(frame)

        # curTime = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
        curTime = time.time()
        fps = 1 / (curTime - prevTime)
        # ffps = cap.get(cv2.CAP_PROP_FPS)
        prevTime = curTime
        cv2.putText(frame, str(int(fps)), (10, 70), fnt, 3, (255, 0, 255), 3)

        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
