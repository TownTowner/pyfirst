import os
import cv2
import numpy as np


def main():
    # # 获取当前工作目录
    # print(os.getcwd())  # 项目目录
    # # 获取脚本所在目录作为基准
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(BASE_DIR, "data\demo.csv")
    # print(file_path)

    # cap = cv2.VideoCapture(0)  # camera
    cap = cv2.VideoCapture("./data/videos/cars.mp4")  # video
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break
        cv2.imshow("frame", frame)
        if cv2.waitKey(1000 // 30) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
