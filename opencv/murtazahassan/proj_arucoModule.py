import cv2
import cv2.aruco as aruco
import numpy as np
import os


def loadImgAugs(path):
    imgDict = {}
    for imgPath in os.listdir(path):
        imgId = os.path.splitext(imgPath)[0]
        imgDict[imgId] = cv2.imread(os.path.join(path, imgPath))

    return imgDict


def findArucoMarkers(img, markerSize=6, totalMakers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # aruco.DICT_4X4_250
    arucoType = getattr(aruco, f"DICT_{markerSize}X{markerSize}_{totalMakers}")
    arucoDict = aruco.getPredefinedDictionary(arucoType)
    arucoParams = aruco.DetectorParameters()
    bboxs, ids, rej = aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    # print(ids)  # None or like [[23]]
    # bboxs
    # (
    #     array(
    #         [[[299.0, 298.0], [260.0, 298.0], [260.0, 257.0], [299.0, 258.0]]],
    #         dtype=float32,
    #     ),
    # )
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return bboxs, ids, rej


def augAruco(img, bbox, aid, imgAug, drawId=True):
    (tl, tr, br, bl) = bbox[0]

    h, w, c = imgAug.shape
    pts1 = np.array([tl, tr, br, bl])  # same as bbox[0]
    pts2 = np.array([[0, 0], [w, 0], [w, h], [0, h]])
    matrix, _ = cv2.findHomography(pts2, pts1)
    imgOut = cv2.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))
    cv2.fillConvexPoly(img, pts1.astype(int), (0, 0, 0))
    imgOut = img + imgOut

    if drawId:
        fnt = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(imgOut, str(aid), tl.astype(int), fnt, 2, (0, 255, 0), 2)

    # cv2.imshow("imgOut", imgOut)
    # cv2.waitKey(0)
    return imgOut


def main():
    cap = cv2.VideoCapture(0)
    # imgAug = cv2.imread("data/imgs/Markers/23.jpg")  # mongo
    imgAugs = loadImgAugs("data/imgs/Markers")  # mongo

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        bboxs, ids, rej = findArucoMarkers(frame)
        # 显式处理None情况以避免numpy数组布尔值判断错误
        ids = ids if ids is not None else []
        for bbox, aid in zip(bboxs, ids):
            # aid = [23]
            k = str(aid[0])
            if k not in imgAugs.keys():
                continue
            frame = augAruco(frame, bbox, aid, imgAugs[k])

        cv2.imshow("frame", frame)
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
