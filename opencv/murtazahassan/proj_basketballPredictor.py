import cv2
import numpy as np
from cvzone.ColorModule import ColorFinder
import cvzone


def main():
    colorFinder = ColorFinder()
    hsvVals = {"hmin": 8, "smin": 96, "vmin": 115, "hmax": 14, "smax": 255, "vmax": 255}
    cap = cv2.VideoCapture("data/videos/bsktbal6.mp4")

    pathListX = []
    pathListY = []
    videoXList = [vx for vx in range(0, 1300)]  # video width
    frameCount = 0
    fnt = cv2.FONT_HERSHEY_PLAIN

    # 视频素材中已知篮筐x的范围为340-430，y的值为590
    bsktY = 590
    bsktXMin = 340
    bsktXMax = 430
    prediction = False

    while cap.isOpened():
        frameCount += 1
        if frameCount == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frameCount = 0
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            pathListX = []
            pathListY = []

        success, img = cap.read()
        if not success:
            break

        # 裁切 图片下方深色内容，防止识别干扰
        img = img[:900, :]

        # find the color of the ball
        imgColor, mask = colorFinder.update(img, hsvVals)
        # find the location of the ball
        imgContours, contours = cvzone.findContours(img, mask, minArea=500)
        if contours and len(contours) > 0:
            # print(f"{contours= } ")
            cx, cy = contours[0]["center"]
            pathListX.append(cx)
            pathListY.append(cy)

        for i in range(len(pathListX)):
            pth = (pathListX[i], pathListY[i])
            cv2.circle(imgContours, pth, 5, (0, 255, 0), cv2.FILLED)
            if i == 0:
                continue
            prePth = (pathListX[i - 1], pathListY[i - 1])
            cv2.line(imgContours, pth, prePth, (0, 255, 0), 2)
        # 预测路径
        A, B, C = 0, 0, 0
        if len(pathListX) > 0:
            A, B, C = np.polyfit(pathListX, pathListY, 2)
            for x in videoXList:
                y = int(A * x**2 + B * x + C)
                cv2.circle(imgContours, (x, y), 5, (255, 0, 255), cv2.FILLED)
        # 预测路径
        if len(pathListX) < 10 and A != 0:
            # Prediction :
            # y = Ax^2 + Bx + C 等价于 0 = Ax^2 + Bx + C - y
            # 又已知y,求x: x = (-B + sqrt(B^2 - 4AC))/2A
            #             x = (-B - sqrt(B^2 - 4AC))/2A
            # x = int((-B + np.sqrt(B**2 - 4 * A * C)) / (2 * A))
            x = int((-B - np.sqrt(B**2 - 4 * A * (C - bsktY))) / (2 * A))
            # Should the predition be changed again
            # when the ball is prediting out of the basket in the next frame?
            # Try to use bsktbal6.mp4 to see the difference.
            # prediction = bsktXMin < x < bsktXMax
            prediction = prediction if prediction else bsktXMin < x < bsktXMax

        predTxt = "Hit!" if prediction else "Miss!"
        predColor = (0, 200, 0) if prediction else (0, 0, 200)
        cvzone.putTextRect(imgContours, predTxt, (50, 100), colorR=predColor)

        imgContours = cv2.resize(imgContours, (0, 0), fx=0.7, fy=0.7)
        # cv2.imshow("img", img)
        # cv2.imshow("mask", mask)
        cv2.imshow("imgContours", imgContours)

        if cv2.waitKey(50) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
