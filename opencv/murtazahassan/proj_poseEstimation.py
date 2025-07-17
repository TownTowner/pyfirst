import cv2
import mediapipe as mp
import mediapipe.python.solutions.pose as mpPose
import mediapipe.python.solutions.drawing_utils as mpDraw
import time


def main():
    prevTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    cap = cv2.VideoCapture("data/videos/dance5.mp4")
    pose = mpPose.Pose()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(
                frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS
            )

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
