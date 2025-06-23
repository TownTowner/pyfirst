import cv2
import numpy as np


def main():
    # Load the image and the watermark image
    img = cv2.imread("./data/imgs/pixpin.png")
    watermark = cv2.imread("./data/imgs/tan.png", cv2.IMREAD_UNCHANGED)

    print(img.shape)
    print(watermark.shape)
    # Resize the watermark image to fit the image size
    watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))
    if watermark.shape[2] == 4:
        watermark = cv2.cvtColor(watermark, cv2.COLOR_BGRA2BGR)
    # print(img[:3, :3, :])

    # 图片与图片的加法，运算结果为：dst = src1 + src2，超出255的部分会被截断
    # cv2.add(img, watermark, dst=img)
    # 图片与数字的加法,运算结果为：dst = src1 + alpha * src2，超出255的部分会被截断
    #   是OpenCV的加法函数，它会进行饱和运算(saturation arithmetic)，当结果超过255时会自动截断为255
    # cv2.add(img, 100, dst=img)
    #   是NumPy的加法运算，它会进行模运算(modulo arithmetic)，当结果超过255时会从0开始重新计算（例如300会变成300-256=44）
    # img += 100

    # addWeighted 加权
    # cv2.addWeighted(img, 0.5, watermark, 0.5, 0, dst=img)

    # 减法
    # cv2.subtract(img, watermark, dst=img)
    # cv2.subtract(img, 100, dst=img)
    # img -= 100
    # 乘法
    # cv2.multiply(img, watermark, dst=img)
    # cv2.multiply(img, 100, dst=img)
    # img *= 100
    # 除法
    # cv2.divide(img, watermark, dst=img)
    # cv2.divide(img, 100, dst=img)
    # img /= 100
    # 取模
    # cv2.mod(img, watermark, dst=img)
    # cv2.mod(img, 100, dst=img)
    # img %= 100

    # 与
    # cv2.bitwise_and(img, watermark, dst=img)
    # 或
    # cv2.bitwise_or(img, watermark, dst=img)
    # 非
    # cv2.bitwise_not(img, dst=img)
    # 异或
    cv2.bitwise_xor(img, watermark, dst=img)

    # print(img[:3, :3, :])
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def watermark():
    # Load the image and the watermark image
    img = cv2.imread("./data/imgs/pixpin.png")

    logo = np.zeros((200, 200, 3), dtype=np.uint8)
    logo[50:80, 50:80] = [0, 255, 0]
    logo[70:100, 70:100] = [0, 0, 255]
    # cv2.imshow("logo", logo)

    # Create a mask for the watermark
    # logo挖孔为白
    mask = np.zeros((200, 200, 3), dtype=np.uint8)
    mask[50:80, 50:80] = [255, 255, 255]
    mask[70:100, 70:100] = [255, 255, 255]
    # cv2.imshow("mask", mask)

    # logo区域变黑
    m = cv2.bitwise_not(mask)
    # cv2.imshow("m", m)

    logo_area = img[:200, :200]
    logo_area = cv2.bitwise_and(logo_area, m)
    # cv2.imshow("logo_area", logo_area)
    # Add the watermark to the image
    img[:200, :200] = cv2.add(logo_area, logo)

    # Show the image with the watermark
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # main()
    watermark()
