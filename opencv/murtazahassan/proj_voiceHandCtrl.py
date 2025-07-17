import cv2
import time
import numpy as np
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# uv add git+https://github.com/AndreMiras/pycaw
import detectorModules as dm


def main():
    # pycaw
    devices = AudioUtilities.GetSpeakers()
    volume = devices.EndpointVolume
    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]
    vol = 0
    volBar = 400
    volPer = 0

    prevTime = 0
    fnt = cv2.FONT_HERSHEY_PLAIN
    fnt_cplx = cv2.FONT_HERSHEY_COMPLEX
    cap = cv2.VideoCapture(0)
    handDetector = dm.HandDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        handDetector.detect(frame)
        handLmDict = handDetector.drawAndFindPosition(frame, handNo=0)
        # print(handLmDict)
        lmList = handLmDict[0]["lms"] if len(handLmDict) > 0 else []
        if len(lmList) != 0:
            # print(lmList[4], lmList[8])

            x1, y1 = thumbTip = lmList[4]
            x2, y2 = indexTip = lmList[8]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(frame, thumbTip, 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, indexTip, 15, (255, 0, 255), cv2.FILLED)
            cv2.line(frame, thumbTip, indexTip, (255, 0, 255), 3)
            cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)
            # print(length)

            # Hand range 50 - 300
            # Volume Range -65 - 0

            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])
            print(int(length), vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(frame, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(frame, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(frame, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        txt = f"{int(volPer)} %"
        cv2.putText(frame, txt, (40, 450), fnt_cplx, 1, (255, 0, 0), 3)

        curTime = time.time()
        fps = 1 / (curTime - prevTime)
        prevTime = curTime
        cv2.putText(frame, str(int(fps)), (10, 70), fnt, 3, (255, 0, 255), 3)

        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
