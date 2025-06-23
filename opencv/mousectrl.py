import cv2
import numpy as np


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下事件
        print(f"Mouse clicked at ({x}, {y},{param = })")  # 打印鼠标点击位置


def main():
    cv2.namedWindow("image")  # 创建一个窗口
    cv2.setMouseCallback("image", mouse_callback, "123")  # 设置鼠标回调函数

    img = np.zeros((512, 512, 3), np.uint8)  # 创建一个空白图像
    while True:
        cv2.imshow("image", img)  # 显示图像
        if cv2.waitKey(1) == ord("q"):  # 按下 'q' 键退出
            break

    cv2.destroyAllWindows()  # 关闭窗口


if __name__ == "__main__":
    main()
