import cv2
import numpy as np
import mediapipe as mp
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as mpDraw
import time


def main():
    hands = mpHands.Hands()
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        h, w, c = frame.shape
        if results.multi_hand_landmarks:
            # print(f"{type(results.multi_hand_landmarks)= }") # list
            # print(f"{results.multi_hand_landmarks= }")
            # results.multi_hand_landmarks= [landmark {
            #   x: 0.504871428
            #   y: 0.65200156
            #   z: 6.48373373e-007
            # }
            # ...
            # landmark {
            #   x: 0.586149931
            #   y: 0.674088955
            #   z: -0.0268904846
            # }]
            for handLms in results.multi_hand_landmarks:
                # print(f"{type(handLms)= }")
                # type(handLms)= <class 'mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList'>
                # print(f"{handLms= }")
                # handLms= landmark {
                #   x: 0.960119247
                #   y: 0.928566039
                #   z: -1.12218652e-006
                # }
                # ...
                # landmark {
                #   x: 0.844297945
                #   y: 0.924705505
                #   z: 0.00306302216
                # }
                for idx, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        # if results.multi_hand_world_landmarks:
        #     for handLms in results.multi_hand_world_landmarks:
        #         mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        # if results.multi_handedness:
        #     for handLms in results.multi_handedness:
        #         mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

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
