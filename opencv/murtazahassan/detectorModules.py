import cv2
import numpy as np
import mediapipe as mp
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.face_detection as mpFace
import mediapipe.python.solutions.face_mesh as mpFaceMsh
import mediapipe.python.solutions.drawing_utils as mpDraw


class HandDetector:
    def __init__(self):
        self.hands = mpHands.Hands()

    def detectAndDraw(self, frame):
        self.results = self.detect(frame)
        return self.draw(frame, self.results)

    def detect(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        return self.results

    def draw(self, frame, results=None):
        h, w, c = frame.shape
        results = results or self.results
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

    def drawAndFindPosition(self, frame, results=None, handNo=None, draw=True):
        self.handLmDict = {}

        results = results or self.results
        h, w, c = frame.shape
        myHands = []
        if handNo is not None and results.multi_hand_landmarks:
            myHands = [results.multi_hand_landmarks[handNo]]

        if len(myHands) == 0:
            return self.handLmDict

        for hIdx, hand in enumerate(myHands):
            xList = []
            yList = []
            for idx, lm in enumerate(hand.landmark):
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.handLmDict[hIdx] = self.handLmDict.get(hIdx, {})
                self.handLmDict[hIdx]["lms"] = self.handLmDict[hIdx].get("lms", {})
                self.handLmDict[hIdx]["lms"][idx] = (cx, cy)
                if draw:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            self.handLmDict[hIdx] = self.handLmDict.get(hIdx, {})
            self.handLmDict[hIdx]["bbox"] = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(
                    frame,
                    (xmin - 20, ymin - 20),
                    (xmax + 20, ymax + 20),
                    (0, 255, 0),
                    2,
                )

        return self.handLmDict


class FaceDetector:
    def __init__(self, fnt=None):
        self.face = mpFace.FaceDetection()
        self.font = fnt or cv2.FONT_HERSHEY_PLAIN

    def detectAndDraw(self, frame):
        results = self.detect(frame)
        return self.draw(frame, results)

    def detect(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(imgRGB)
        return results

    def draw(self, frame, results):
        ih, iw, ic = frame.shape
        detections = results.detections or []
        for detection in detections:
            # print(f"{detection= }")
            #  detection= label_id: 0
            # score: 0.922280312
            # location_data {
            #   format: RELATIVE_BOUNDING_BOX
            #   relative_bounding_box {
            #     xmin: 0.554067671
            #     ymin: 0.521598577
            #     width: 0.127527
            #     height: 0.226714432
            #   }
            #   relative_keypoints {
            #     x: 0.595507801
            #     y: 0.570104301
            #   }
            #   relative_keypoints {
            #     x: 0.648964167
            #     y: 0.595219374
            #   }
            #   relative_keypoints {
            #     x: 0.617281318
            #     y: 0.634479344
            #   }
            #   relative_keypoints {
            #     x: 0.611289084
            #     y: 0.682459056
            #   }
            #   relative_keypoints {
            #     x: 0.559694707
            #     y: 0.585343063
            #   }
            #   relative_keypoints {
            #     x: 0.676331162
            #     y: 0.634479463
            #   }
            # }
            bbox = detection.location_data.relative_bounding_box
            xmin, ymin, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            xmin, ymin, w, h = (
                int(xmin * iw),
                int(ymin * ih),
                int(w * iw),
                int(h * ih),
            )
            # mpDraw.draw_detection(frame, detection)
            cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 3)
            txt = f"{int(detection.score[0] * 100)}%"
            cv2.putText(frame, txt, (xmin, ymin - 10), self.font, 3, (255, 0, 255), 3)


class FaceMeshDetector:
    def __init__(
        self,
        static_image_mode=False,
        max_num_faces=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        connections=None,
        lmDrawSpec=None,
        connDrawSpec=None,
        fnt=None,
    ):
        self.faceMesh = mpFaceMsh.FaceMesh(
            static_image_mode=static_image_mode,
            max_num_faces=max_num_faces,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )
        self.connections = connections
        self.lmDrawSpec = lmDrawSpec
        self.connDrawSpec = connDrawSpec

        self.font = fnt or cv2.FONT_HERSHEY_PLAIN

    def detectAndDraw(self, frame):
        results = self.detect(frame)
        return self.draw(frame, results)

    def detect(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        return results

    def draw(self, frame, results):
        lms = results.multi_face_landmarks or []
        # print(f"{len(results.multi_face_landmarks)= }")
        for lm in lms:
            # print(f"{len(faceLms.landmark)= }")
            mpDraw.draw_landmarks(
                frame, lm, self.connections, self.lmDrawSpec, self.connDrawSpec
            )
