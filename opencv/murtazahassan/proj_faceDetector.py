import cv2
import numpy as np
import dlib


def createCropBBox(img, points, scale=5, masking=False, cropping=True):
    mask = np.zeros_like(img)
    if masking:
        mask = cv2.fillPoly(mask, [points], (255, 255, 255))
        img = cv2.bitwise_and(img, mask)
        # cv2.imshow("mask", img)
    if cropping:
        bbox = cv2.boundingRect(points)
        x, y, w, h = bbox
        imgCrop = img[y : y + h, x : x + w]
        imgCrop = cv2.resize(imgCrop, (0, 0), None, scale, scale)
        return imgCrop
    else:
        return mask


def main():
    faceDetector = dlib.get_frontal_face_detector()

    # download from https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    # visit for all: https://dlib.net/files
    predictor = dlib.shape_predictor("config/shape_predictor_68_face_landmarks.dat")

    fnt = cv2.FONT_HERSHEY_SIMPLEX
    cv2.namedWindow("BGR")
    cv2.resizeWindow("BGR", 640, 240)
    cv2.createTrackbar("Blue", "BGR", 0, 255, lambda x: x)
    cv2.createTrackbar("Green", "BGR", 0, 255, lambda x: x)
    cv2.createTrackbar("Red", "BGR", 0, 255, lambda x: x)

    while True:
        img = cv2.imread("data/imgs/model.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector(gray)
        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            # cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 2)

            points = []
            landmarks = predictor(gray, face)
            # print(f"{(landmarks.parts())= }")
            for idx, point in enumerate(landmarks.parts()):
                # cv2.circle(img, (point.x, point.y), 2, (0, 0, 255), 2)
                # cv2.putText(img, str(idx), (point.x, point.y), fnt, 0.5, (255, 0, 0), 1)
                points.append([point.x, point.y])

            points = np.array(points)
            # 36:42 -> left eye; 48:68 -> mouth
            imgLips = createCropBBox(img, points[48:61], masking=True, cropping=False)
            # cv2.imshow("Lips", imgLips)
            imgColoredLips = np.zeros_like(imgLips)
            # imgColoredLips[:] = 153, 0, 157
            b = cv2.getTrackbarPos("Blue", "BGR")
            g = cv2.getTrackbarPos("Green", "BGR")
            r = cv2.getTrackbarPos("Red", "BGR")
            imgColoredLips[:] = b, g, r
            imgColoredLips = cv2.bitwise_and(imgLips, imgColoredLips)
            # 模糊边界，更自然
            imgColoredLips = cv2.GaussianBlur(imgColoredLips, (7, 7), 10)
            grayImg = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            imgColoredLips = cv2.addWeighted(grayImg, 1, imgColoredLips, 0.4, 0)
            cv2.imshow("BGR", imgColoredLips)

        cv2.imshow("face", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
