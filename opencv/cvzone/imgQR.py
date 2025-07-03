import cv2
from typing import List
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode, Decoded
import barcode
from barcode.writer import ImageWriter


def generateQRCode(data, filename, size=(500, 500)):
    # 创建二维码生成器
    qr = cv2.QRCodeEncoder().create()
    qr_image = qr.encode(data)
    # 调整图片大小
    if size is not None:
        qr_image = cv2.resize(qr_image, size, interpolation=cv2.INTER_AREA)
    # 保存二维码图片
    cv2.imwrite(filename, qr_image)
    cv2.waitKey(0)


def generateBarCode(data, filename, ext="png", size=(500, 500)):
    # 生成EAN13格式的条形码
    ean = barcode.get("ean13", data, writer=ImageWriter(format=ext))
    filename = ean.save(filename)
    print(f"条形码已保存为: {filename}")


def readQRCode(filename):
    img = cv2.imread(filename)
    qrcodes: List[Decoded] = decode(img)
    print(qrcodes)
    fnt = cv2.FONT_HERSHEY_SIMPLEX

    for qrcode in qrcodes:
        txt = qrcode.data.decode("utf-8")
        print(txt)
        pts = np.array(qrcode.polygon, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        x, y, w, h = qrcode.rect
        cv2.putText(img, txt, (x, y - 10), fnt, 1, (0, 0, 255), 2)
    cv2.imshow("img", img)
    cv2.waitKey()


def readCapQR():
    cap = cv2.VideoCapture(0)
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        qrcodes: List[Decoded] = decode(frame)
        for qrcode in qrcodes:
            txt = qrcode.data.decode("utf-8")
            print(txt)
            pts = np.array(qrcode.polygon, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
            x, y, w, h = qrcode.rect
            cv2.putText(frame, txt, (x, y - 10), fnt, 1, (0, 0, 255), 2)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()


def main():
    qrcode_path = "data/imgs/qr_pyzbar.png"
    bar_file = "data/imgs/bar_pyzbar"
    bar_ext = "png"
    bar_path = f"{bar_file}.{bar_ext}"

    # generateQRCode("pyzbar", qrcode_path)
    # generateBarCode("123456789012", bar_file, ext=bar_ext)
    # readQRCode(qrcode_path)
    # readCapQR()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
