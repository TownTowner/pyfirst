import cv2
import mediapipe.python.solutions.face_mesh as faceMsh
import mediapipe.python.solutions.drawing_utils as mpDraw
import time


def main():
    prevTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    cap = cv2.VideoCapture("data/videos/face5.mp4")
    faceMesh = faceMsh.FaceMesh(
        max_num_faces=6, min_detection_confidence=0.2, min_tracking_confidence=0.2
    )
    lmDrawSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
    connDrawSpec = mpDraw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1)
    connections = faceMsh.FACEMESH_CONTOURS
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            # print(f"{len(results.multi_face_landmarks)= }")
            for faceLms in results.multi_face_landmarks:
                # print(f"{len(faceLms.landmark)= }")
                mpDraw.draw_landmarks(
                    frame, faceLms, connections, lmDrawSpec, connDrawSpec
                )

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
