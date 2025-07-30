import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


def main():
    cap = cv2.VideoCapture("data/videos/blink.mp4")
    detector = FaceMeshDetector(maxFaces=1)
    idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
    blinkCounter = 0
    counter = 0
    blinkRatio = 0
    ratioList = []
    color = (255, 0, 255)

    while cap.isOpened():
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        if not success:
            break

        img, faces = detector.findFaceMesh(img, draw=False)

        if faces and len(faces) > 0:
            face = faces[0]
            for id in idList:
                cv2.circle(img, face[id], 2, (0, 255, 0), cv2.FILLED)

            leftUp = face[159]
            leftDown = face[23]
            leftLeft = face[130]
            leftRight = face[243]
            lenghtVer, _ = detector.findDistance(leftUp, leftDown)
            lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

            cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
            cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

            ratio = int((lenghtVer / lenghtHor) * 100)
            ratioList.append(ratio)
            
            if len(ratioList) > 3:
                ratioList.pop(0)
            ratioAvg = sum(ratioList) / len(ratioList)

            if ratioAvg < 35 and counter == 0:
                blinkCounter += 1
                color = (0, 200, 0)
                counter = 1
            if counter != 0:
                counter += 1
                if counter > 10:
                    counter = 0
                    color = (255, 0, 255)

            txt = f"Blink Count: {blinkCounter}"
            cvzone.putTextRect(img, txt, (50, 100), colorR=color)

        cv2.imshow("Image", img)

        key = cv2.waitKey(10) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
