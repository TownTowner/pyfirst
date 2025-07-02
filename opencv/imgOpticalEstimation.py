import cv2
from cv2.typing import MatLike
import numpy as np


def main():
    cap = cv2.VideoCapture("data/videos/walking.mp4")
    ret, frame = cap.read()
    if not ret:
        raise Exception("视频读取失败")

    prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_corners = cv2.goodFeaturesToTrack(prev_gray, 100, 0.3, 7)
    if prev_corners is None:
        raise Exception("角点检测失败")

    mask = np.zeros_like(frame)
    color = np.random.randint(0, 255, (100, 3))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 光流检测
        corners, status, err = cv2.calcOpticalFlowPyrLK(
            prev_gray, gray, prev_corners, None, (15, 15)
        )
        # print(f"{status= }")
        # 筛选出好的点
        good_corners = corners[status == 1]
        prev_good_corners = prev_corners[status == 1]

        # print(f"{good_corners= }")
        # 绘制轨迹
        for i, (new, prev) in enumerate(zip(good_corners, prev_good_corners)):
            a, b = new.ravel().astype(int)
            c, d = prev.ravel().astype(int)
            # print(f"{a= },{b= }")
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

        img = cv2.add(frame, mask)
        cv2.imshow("frame", img)

        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

        # 更新上一帧
        prev_gray = gray.copy()
        prev_corners = good_corners.reshape(-1, 1, 2)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
