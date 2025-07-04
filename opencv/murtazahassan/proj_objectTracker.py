import cv2
import numpy as np


def main():
    classNames = []
    with open("config/ObjectTracker/coco.names", "r") as f:
        classNames = f.read().splitlines()
    # print(classNames)
    configPath = "config/ObjectTracker/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    weightsPath = "config/ObjectTracker/frozen_inference_graph.pb"

    conf_thresh = 0.5
    nms_thresh = 0.4
    net = cv2.dnn.DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    fnt = cv2.FONT_HERSHEY_COMPLEX
    color = (0, 255, 0)

    # img = cv2.imread("data/imgs/lena.png")
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("data/videos/walking.mp4")
    while True:
        success, img = cap.read()
        if not success:
            break

        classIds, confs, bbox = net.detect(img, confThreshold=conf_thresh)
        # print(classIds, bbox)
        if len(classIds) <= 0:
            continue

        # cv2.dnn.NMSBoxes 是OpenCV中用于执行非极大值抑制(Non-Maximum Suppression, NMS)的函数，主要用于目标检测任务中去除冗余的边界框
        # 函数作用：
        # 1. 首先过滤掉置信度低于 conf_thresh 的边界框
        # 2. 然后对剩余的边界框，根据置信度分数从高到低排序
        # 3. 对于重叠度(IOU)高于 nms_thresh 的边界框，只保留置信度最高的那个
        # 4. 返回保留的边界框的索引列表
        indices = cv2.dnn.NMSBoxes(bbox, confs.flatten(), conf_thresh, nms_thresh)
        # print(f"{indices= }")
        # for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        for i in indices:
            box = bbox[i]
            classId = classIds[i]
            confidence = confs[i]
            cv2.rectangle(img, box, color=color, thickness=2)
            cls_name = classNames[classId - 1]
            conf = str(round(confidence * 100, 2))
            txt = f"{cls_name} : {conf}%"
            cv2.putText(img, txt, (box[0] + 10, box[1] + 30), fnt, 1, color, 2)

        cv2.imshow("img", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
