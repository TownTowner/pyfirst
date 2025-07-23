import cv2
import numpy as np
import cvzone
from cvzone.ColorModule import ColorFinder
import pickle

colorFinder = ColorFinder()
cornerPoints = [[377, 52], [944, 71], [261, 624], [1058, 612]]
hsvVals = {"hmin": 30, "smin": 34, "vmin": 0, "hmax": 41, "smax": 255, "vmax": 255}


def getBoard(img):
    width, height = int(400 * 1.5), int(380 * 1.5)
    pts1 = np.float32(cornerPoints)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    for x in range(4):
        cv2.circle(img, tuple(cornerPoints[x]), 15, (0, 255, 0), cv2.FILLED)

    return imgOutput


def detectColorDarts(img):
    imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
    imgColor, mask = colorFinder.update(imgBlur, hsvVals)
    # 去噪点
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    mask = cv2.dilate(mask, kernel, iterations=2)
    kernel_c = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_c)
    # cv2.imshow("imgColor", imgColor)
    return imgColor, mask


def loadDartPolygons():
    with open("data/velcro_dart_polygons", "rb") as f:
        dartPolygons = pickle.load(f)
    return dartPolygons


def main():
    dartPolygons = loadDartPolygons()
    # print(f"{dartPolygons= }")

    # trackBar=True : will print the trackbar values
    cap = cv2.VideoCapture("data/videos/velcro2.mp4")
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 70)
    frameCount = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    # 连续的帧检测到目标的次数
    frameContourHitCount = 0
    imgDetectList = []
    prevDetectImgFull = None
    hitDrawBallList = []
    totalScore = 0

    while cap.isOpened():
        frameCount += 1
        if frameCount == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frameCount = 0
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            prevDetectImgFull = None
            imgDetectList = []
            frameContourHitCount = 0
            hitDrawBallList = []
            totalScore = 0
            # cv2.destroyWindow("prevDetectImgFull")

        success, img = cap.read()
        if not success:
            break

        imgBoard = getBoard(img)
        imgColor, mask = detectColorDarts(imgBoard)

        mask_back = mask
        if prevDetectImgFull is not None:
            mask = mask - prevDetectImgFull
            # cv2.imshow("prevDetectImgFull", prevDetectImgFull)

        # contours : [{"cnt": cnt, "area": area, "bbox": [x, y, w, h], "center": [cx, cy]}]
        imgContours, contours = cvzone.findContours(imgBoard, mask, minArea=3500)
        # 连续的帧检测到目标的次数
        if len(contours) != 0:
            frameContourHitCount += 1
        else:
            frameContourHitCount = 0

        if len(contours) > 0 and frameContourHitCount >= 10:
            # print("检测到目标")
            imgDetectList.append(mask)
            prevDetectImgFull = mask_back
            frameContourHitCount = 0
            # print(f"{contours= }")  #
            center = contours[0]["center"]
            bbox = contours[0]["bbox"]
            # print(f"{bbox= }, {center= }")
            for polyScore in dartPolygons:
                path, score = polyScore
                # print(f"{polyScore= }")  # [path,score]
                poly = np.array([path], np.int32)
                inside = cv2.pointPolygonTest(poly, center, False)
                if inside >= 1:
                    print(f"{center= }, {polyScore[1]= }: {inside= }")
                    # imgContours = cv2.polylines(
                    #     imgContours, [poly], True, (0, 255, 0), 2
                    # )
                    hitDrawBallList.append([bbox, center, poly])
                    totalScore += score

                    print(f"{totalScore= }")
        for bbox, center, poly in hitDrawBallList:
            cv2.rectangle(imgContours, bbox, (0, 255, 0), 2)
            cv2.circle(imgContours, center, 5, (255, 0, 0), cv2.FILLED)
            cv2.drawContours(imgContours, poly, -1, (0, 255, 0), cv2.FILLED)

        cv2.putText(
            imgContours, f"Score: {totalScore}", (0, 30), fnt, 2, (255, 0, 0), 3
        )

        # cv2.imshow("img", img)
        # cv2.imshow("imgBoard", imgBoard)
        cv2.imshow("imgContours", imgContours)
        # cv2.imshow("mask", mask)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
