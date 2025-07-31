import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


def calcArgs(img):
    pass


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # 原理图：data/imgs/Distance-measurement.png
    # 计算公式原理: focalLength / 像素高（宽）度 = 距离 / 实际高（宽）度
    #           距离 =  focalLength * 实际高（宽）度 / 像素高（宽）度

    detector = FaceMeshDetector()
    realDistance = 50  # cm
    realW = 6.3  # avrage eye's width in cm
    fnt = cv2.FONT_HERSHEY_PLAIN

    # calced by the temp code below
    focalLength = 800

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        img, faces = detector.findFaceMesh(img, draw=False)
        if faces and len(faces) > 0:
            face = faces[0]
            # print(len(face))  # 468
            leftEye = face[374]  # eye bottom point
            rightEye = face[145]  # eye bottom point
            cv2.line(img, leftEye, rightEye, (0, 255, 0), 2)
            cv2.circle(img, leftEye, 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, rightEye, 5, (255, 0, 0), cv2.FILLED)

            pixWidth, *_ = detector.findDistance(leftEye, rightEye)

            # calc focalLength (temporary):
            # focalLength = (pixWidth * realDistance) / realW
            # print(f"{pixWidth= }, {focalLength= }")
            # output: pixWidth= 101.07917688624102, focalLength= 802.2156895733415

            distance = (focalLength * realW) / pixWidth
            txt = f"{distance:.2f} cm"
            middelhead = face[10]
            cv2.putText(img, txt, middelhead, fnt, 2, (0, 255, 0), 3)

        cv2.imshow("img", img)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
