import cv2
import numpy as np
import mediapipe as mp
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as mpDraw
import time


class HandDetector:
    def __init__(self):
        self.hands = mpHands.Hands()

    def detectAndDraw(self, frame):
        results = self.detect(frame)
        return self.draw(frame, results)

    def detect(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        return results

    def draw(self, frame, results):
        h, w, c = frame.shape
        lms = results.multi_hand_landmarks or []
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
        for handLms in lms:
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
        return frame
