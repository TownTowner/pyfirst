import cv2
import numpy as np
import pytesseract


def main():
    carplate_path = (
        "config/cascade_detection_files/haarcascade_russian_plate_number.xml"
    )
    carplate_cascade = cv2.CascadeClassifier(carplate_path)  # ,1.2,4

    img = cv2.imread("data/imgs/carplate.png")
    img = cv2.imread("data/imgs/carplate_suD.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    carplates = carplate_cascade.detectMultiScale(gray)

    print(f"{len(carplates) = }")
    for x, y, w, h in carplates:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        cv2.imshow("roi_gray", roi_gray)

        # 二值化
        thresh_t = cv2.THRESH_BINARY | cv2.THRESH_OTSU
        ret, thresh = cv2.threshold(roi_gray, 0, 255, thresh_t)
        # 开操作
        kernel = np.ones((3, 3), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        cv2.imshow("thresh", thresh)
        result = pytesseract.image_to_string(
            thresh, lang="chi_sim+eng", config="--psm 8 --oem 3"
        )
        print(f"{result= }")

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
