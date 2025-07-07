import cv2
import numpy as np


def findObjects(img, outputs, classNames):
    iw, ih = img.shape[1], img.shape[0]
    bbox = []
    classIds = []
    confs = []
    thres = 0.5
    nmsThres = 0.2
    for output in outputs:
        for det in output:
            # det: cx, xy, w, h, confidence, score1,score2,...,scoreN
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence <= thres:
                continue

            w, h = int(det[2] * iw), int(det[3] * ih)
            x, y = int(det[0] * iw - w / 2), int(det[1] * ih - h / 2)
            bbox.append([x, y, w, h])
            classIds.append(classId)
            confs.append(float(confidence))

    print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nmsThres)
    print(indices)
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    for i in indices:
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        txt = f"{classNames[classIds[i]]} : {int(confs[i] * 100)}%"
        cv2.putText(img, txt, (x, y - 10), fnt, 0.6, (255, 0, 255), 2)


def main():
    classNames = []
    classFile = "config/ObjectTracker/coco.names"
    with open(classFile, "rt") as f:
        classNames = f.read().splitlines()
    # print(classNames)

    # load model
    configPath = "config/yolo/yolov3.cfg"
    weightsPath = "config/yolo/yolov3.weights"
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break

        blob = cv2.dnn.blobFromImage(img, 1 / 255, (320, 320), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        # print(net.getLayerNames())
        layerNames = net.getUnconnectedOutLayersNames()
        # print(f"{layerNames= }")
        outputs = net.forward(layerNames)
        # print(outputs[0].shape)
        # print(outputs[1].shape)
        # print(outputs[2].shape)
        # print(f"{outputs[0][0]= }")

        findObjects(img, outputs, classNames)

        cv2.imshow("img", img)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
