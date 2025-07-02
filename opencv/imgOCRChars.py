import cv2
import numpy as np
from PIL import Image
import pytesseract


def ocrChars():
    img = cv2.imread("data/imgs/chars.png")
    imgH, imgW = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    data = pytesseract.image_to_boxes(thresh)
    # print(data)
    # output:
    # M 88 411 198 511 0
    # u 221 409 281 485 0

    # 解析数据
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    for d in data.splitlines():
        d = d.split(" ")
        x, y, w, h = int(d[1]), int(d[2]), int(d[3]), int(d[4])
        # imgH - y 是因为 y 是从下往上数的，而图片是从上往下数的：
        # - Tesseract OCR的 image_to_boxes() 方法返回的坐标系统原点在图像左下角 ，y轴向上
        # - OpenCV的图像坐标系原点在 左上角 ，y轴向下
        cv2.rectangle(img, (x, imgH - y), (w, imgH - h), (0, 255, 0), 2)
        cv2.putText(img, d[0], (x, imgH - y + 25), fnt, 1, (0, 255, 0), 2)
    # 显示
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ocrWord():
    img = cv2.imread("data/imgs/chars.png")
    imgH, imgW = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    cfg = ""
    # cfg = "--oem 3 --psm 6 outputbase digits"  # digit only
    data = pytesseract.image_to_data(thresh, config=cfg)
    # print(data)
    # output:
    # level   page_num block_num par_num line_num   word_num   left    top  width  height   conf      text
    # 1       1         0         0       0         0          0       0    1519   590     -1
    # 2       1         1         0       0         0          88      71   1307   251     -1
    # 3       1         1         1       0         0          88      71   1307   251     -1
    # 4       1         1         1       1         0          88      71   1307   136     -1
    # 5       1         1         1       1         1          88      71   613    110     78.483017  Murtaza's
    # 5       1         1         1       1         2          748     73   647    134     96.843147  Workshop
    # 4       1         1         1       2         0          402     249  556    73      -1
    # 5       1         1         1       2         1          402     249  355    73      92.661324  Robotics
    # 5       1         1         1       2         2          790     249  61     73      92.661324  &
    # 5       1         1         1       2         3          881     254  77     66      96.948090  Al
    # 2       1         2         0       0         0          35      462  1407   69      -1
    # 3       1         2         1       0         0          35      462  1407   69      -1
    # 4       1         2         1       1         0          35      462  1407   69      -1
    # 5       1         2         1       1         1          35      462  1407   69      89.642715  123456789101112131415

    # 解析数据
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    # 过滤第一行(列名)
    for b in data.splitlines()[1:]:
        d = b.split()
        # print(d)
        # 过滤未识别出内容的行
        if len(d) < 12:
            continue
        x, y, w, h = int(d[6]), int(d[7]), int(d[8]), int(d[9])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, d[11], (x, y - 5), fnt, 1, (0, 255, 0), 2)
    # 显示
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # ocrChars()
    ocrWord()


if __name__ == "__main__":
    main()
