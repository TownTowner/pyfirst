import cv2
import mediapipe.python.solutions.face_mesh as faceMsh
import mediapipe.python.solutions.drawing_utils as mpDraw
import time
import detectorModules as dm


def main():
    cap = cv2.VideoCapture("data/videos/face3.mp4")

    connections = faceMsh.FACEMESH_CONTOURS
    lmDrawSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
    connDrawSpec = mpDraw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1)
    fnt = cv2.FONT_HERSHEY_PLAIN

    faceMesh = dm.FaceMeshDetector(
        max_num_faces=6,
        min_detection_confidence=0.2,
        min_tracking_confidence=0.2,
        connections=connections,
        lmDrawSpec=lmDrawSpec,
        connDrawSpec=connDrawSpec,
        fnt=fnt,
    )

    prevTime = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        faceMesh.detectAndDraw(frame)

        curTime = time.time()
        fps = 1 / (curTime - prevTime)
        prevTime = curTime
        cv2.putText(frame, str(int(fps)), (10, 70), fnt, 3, (255, 0, 255), 3)

        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
