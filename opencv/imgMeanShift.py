import cv2
import numpy as np


def meanShift():
    img = cv2.imread("data/imgs/flower.png")
    img = cv2.imread("data/imgs/keys.png")
    imgMean = cv2.pyrMeanShiftFiltering(img, 10, 50)
    imgCanny = cv2.Canny(imgMean, 100, 200)

    # 找轮廓
    contours, hierarchy = cv2.findContours(
        imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 轮廓绘制
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    cv2.imshow("result", np.hstack((img, imgMean)))
    cv2.imshow("canny", imgCanny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mog2():
    # cap = cv2.VideoCapture("data/videos/people.mp4")
    cap = cv2.VideoCapture("data/videos/walking.mp4")
    mog = cv2.createBackgroundSubtractorMOG2()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        fgmask = mog.apply(frame)
        cv2.imshow("mog", fgmask)
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def cascadeDetection():
    detect_file_path = "config/cascade_detection_files/haarcascade_fullbody.xml"
    body_classifier = cv2.CascadeClassifier(detect_file_path)

    # Initiate video capture for video file, here we are using the video file in which pedestrians would be detected
    # cap = cv2.VideoCapture("data/videos/people.mp4")
    cap = cv2.VideoCapture("data/videos/walking2.mp4")

    # Loop once video is successfully loaded
    while cap.isOpened():

        # Reading the each frame of the video
        ret, frame = cap.read()

        # here we are resizing the frame, to half of its size, we are doing to speed up the classification
        # as larger images have lot more windows to slide over, so in overall we reducing the resolution
        # of video by half that’s what 0.5 indicate, and we are also using quicker interpolation method that is #interlinear
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Pass frame to our body classifier
        bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

        # Extract bounding boxes for any bodies identified
        for x, y, w, h in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.imshow("Pedestrians", frame)

        if cv2.waitKey(100) == 13:  # 13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()


def imgFix():
    img = cv2.imread("data/imgs/fruits.png")
    mask = cv2.imread("data/imgs/fruits_lines.png", cv2.IMREAD_GRAYSCALE)
    # mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
    print(mask.shape)
    print(img.shape)
    res = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

    cv2.imshow("img", np.hstack((img, res)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # meanShift()
    # mog2()
    # cascadeDetection()
    imgFix()


if __name__ == "__main__":
    main()
