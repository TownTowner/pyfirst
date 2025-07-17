import cv2
import mediapipe as mp
import mediapipe.python.solutions.face_detection as mpFace
import mediapipe.python.solutions.drawing_utils as mpDraw
import time


def main():
    prevTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    cap = cv2.VideoCapture("data/videos/face1.mp4")
    faser = mpFace.FaceDetection()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        ih, iw, ic = frame.shape
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = faser.process(imgRGB)
        if results.detections:
            for detection in results.detections:
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
                cv2.putText(frame, txt, (xmin, ymin - 10), fnt, 3, (255, 0, 255), 3)

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
