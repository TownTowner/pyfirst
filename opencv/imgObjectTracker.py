# OpenCV上有八种不同的目标追踪算法：
# BOOSTING Tracker：和Haarcascades（AdaBoost）背后所用的机器学习算法相同，但是距其诞生已有十多年
# 了。这一追踪器速度较慢，并且表现不好。（最低支持OpenCV3.0.0）
# MIL Tracker：比上一个追踪器更精确，但是失败率比较高。（最低支持OpenCV3.0.0）
# KCF Tracker：比BOOSTING和MIL都快，但是在有遮挡的情况下表现不佳。（最低支持OpenCV3.1.0）
# CSRT Tracker:比KCF稍精确，但速度不如后者。（最低支持OpenCV3.4.2）
# MedianFlow Tracker：出色的跟踪故障报告。当运动是可预测的并且没有遮挡时，效果非常好，但是对于快速跳
# 动或快速移动的物体，模型会失效。（最低支持OpenCV3.0.0）
# TLD Tracker：在多帧遮挡下效果最好。但是TLD的误报非常多，所以不推荐。（最低支持OpenCV3.0.0）
# MOSSE Tracker：速度真心快，但是不如CSRT和KCF的准确率那么高，如果追求速度选它准没错。（最低支持
# OpenCV 3.4.1）
# GOTURN Tracker：这是OpenCV中唯一一深度学习为基础的目标检测器。它需要额外的模型才能运行。（最低
# 支持OpenCV3.2.0）

from typing import List
import cv2
import numpy as np


def legacy():
    print(f"{(cv2.__version__)}")  # opencv V4.5.5
    # print([attr for attr in dir(cv2) if "Tracker" in attr])

    # "TrackerCSRT", "TrackerCSRT_Params", "TrackerCSRT_create",
    # "TrackerDaSiamRPN", "TrackerDaSiamRPN_Params", "TrackerDaSiamRPN_create",
    # "TrackerGOTURN", "TrackerGOTURN_Params", "TrackerGOTURN_create",
    # "TrackerKCF", "TrackerKCF_CN", "TrackerKCF_CUSTOM",
    # "TrackerKCF_GRAY", "TrackerKCF_Params", "TrackerKCF_create",
    # "TrackerMIL", "TrackerMIL_Params", "TrackerMIL_create",
    # "legacy_MultiTracker"

    trackers = cv2.legacy.MultiTracker_create()  # opencv V4.5.5
    # print(dir(cv2.legacy))
    # "MultiTracker_create", "TrackerBoosting_create", "TrackerCSRT_create",
    # "TrackerKCF_create", "TrackerMIL_create", "TrackerMOSSE_create",
    # "TrackerMedianFlow_create", "TrackerTLD_create",
    tracker_dict = {
        "boosting": cv2.legacy.TrackerBoosting_create,
        "mil": cv2.legacy.TrackerMIL_create,
        "kcf": cv2.legacy.TrackerKCF_create,
        "csrt": cv2.legacy.TrackerCSRT_create,
        "medianflow": cv2.legacy.TrackerMedianFlow_create,
        "tld": cv2.legacy.TrackerTLD_create,
        "mosse": cv2.legacy.TrackerMOSSE_create,
    }

    # tracker = cv2.legacy.TrackerGOTURN_create()
    # trackers.add(tracker, frame, bbox)

    # cap = cv2.VideoCapture("data/videos/soccer.mp4")
    cap = cv2.VideoCapture("data/videos/racecar.mp4")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break

        success, boxes = trackers.update(frame)
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(100) & 0xFF
        if k == ord("s"):
            roi = cv2.selectROI("frame", frame)
            tracker = tracker_dict["csrt"]()
            trackers.add(tracker, frame, roi)
        elif k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def current():
    print(f"{(cv2.__version__)}")

    # print([attr for attr in dir(cv2) if "Tracker" in attr])
    class SimpleMultiTracker:
        trackers: List[cv2.Tracker] = []

        def __init__(self):
            pass

        def add(self, tracker, frame, bbox):
            tracker.init(frame, bbox)
            self.trackers.append(tracker)

        def update(self, frame):
            boxes = []
            for tracker in self.trackers:
                success, box = tracker.update(frame)
                if success:
                    boxes.append(box)
            return True, boxes

    # 使用示例
    trackers = SimpleMultiTracker()
    tracker_dict = {
        # "boosting": cv2.TrackerBoosting,
        "mil": cv2.TrackerMIL().create,
        "kcf": cv2.TrackerKCF().create,
        "csrt": cv2.TrackerCSRT().create,
        # "medianflow": cv2.TrackerMedianFlow,
        # "tld": cv2.TrackerTLD,
        # "mosse": cv2.TrackerMOSSE,
        "nano": cv2.TrackerNano().create,
        "vit": cv2.TrackerVit().create,
    }

    # cap = cv2.VideoCapture("data/videos/soccer.mp4")
    cap = cv2.VideoCapture("data/videos/racecar.mp4")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break

        success, boxes = trackers.update(frame)
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(100) & 0xFF
        if k == ord("s"):
            roi = cv2.selectROI("frame", frame)
            # cv2.TrackerCSRT().init(frame,roi)
            tracker = tracker_dict["csrt"]()
            trackers.add(tracker, frame, roi)
        elif k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    v = cv2.__version__.split(".")
    v = float(f"{v[0]}.{v[1]}")

    if v > 4.5:
        current()
    elif v <= 4.5:
        legacy()


if __name__ == "__main__":
    main()
