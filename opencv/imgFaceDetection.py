import cv2
import numpy as np


def main():
    # face_dft_path = "config/cascade_detection_files/haarcascade_frontalface_default.xml"
    # face_cascade = cv2.CascadeClassifier(face_dft_path) # ,1.3,5

    face_alt2_path = "config/cascade_detection_files/haarcascade_frontalface_alt2.xml"
    face_cascade = cv2.CascadeClassifier(face_alt2_path)  # ,1.2,4

    eye_cfg_path = "config/cascade_detection_files/haarcascade_eye.xml"
    eye_cascade = cv2.CascadeClassifier(eye_cfg_path)

    # img = cv2.imread("data/imgs/faces.jpg")
    img = cv2.imread("data/imgs/20CTs_physicists.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    print(f"{len(faces) = }")
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
