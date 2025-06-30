import cv2
import numpy as np


def calcuCenter(rec):
    x, y, w, h = rec
    cx = int((x + x + w) / 2)
    cy = int((y + y + h) / 2)
    return cx, cy


def main():
    videoPath = "./data/videos/car4.ts"
    videoPath = "./data/videos/cars.mp4"
    # videoPath = 0
    cap = cv2.VideoCapture(videoPath)
    # 去除背景,4.X已移除
    # mod = cv2.bgsegm.createBackgroundSubtractorMOG()
    # 对光照变化和动态背景的适应性更好，但对阴影的检测能力较弱。
    # mod = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    mod = cv2.createBackgroundSubtractorKNN(detectShadows=False)
    setk = (5, 5)
    # 标准线
    lineHigh = 400
    # 偏移量
    offset = 6
    # 计数器
    carCount = 0
    # 添加车辆跟踪字典（id: 是否已计数）
    tracked_cars = {}
    # # 检测区域
    # detectArea = [(0, lineHigh), (1280, lineHigh)]
    # # 检测线
    # detectLine = [(320, lineHigh - offset), (960, lineHigh - offset)]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, setk)
    while True:
        ret, frame = cap.read()  # Read a frame from the video
        if not ret:
            break  # Break the loop if no frame is read (end of video)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, setk, 5)
        fmask = mod.apply(blur)

        # print("Unique before in mask:", np.unique(fmask))
        # # 去除阴影
        # _, fmask = cv2.threshold(fmask, 254, 255, cv2.THRESH_BINARY)
        # _, fmask = cv2.threshold(fmask, 127, 255, cv2.THRESH_BINARY)
        # cv2.imshow("Foreground Mask", fmask)
        # print("Unique values in mask:", np.unique(fmask))  # 应该只有0和255两个值

        erode = cv2.erode(fmask, kernel)  # 腐蚀
        dilate = cv2.dilate(erode, kernel, iterations=2)  # 膨胀
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)  # 闭运算

        # cv2.imshow("merge", np.hstack((erode, dilate, close)))
        # 检测线
        cv2.line(frame, (0, lineHigh), (1280, lineHigh), (0, 0, 255), 2)

        contours, _ = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            rec = cv2.boundingRect(cnt)
            x, y, w, h = rec
            # if h > 50 and w > 90:
            if area <= 1000:
                continue

            # 为每辆车生成唯一ID(通过轮廓跟踪实现)（示例用简单递增，实际可结合轮廓匹配）
            car_id = hash(cnt.tobytes())

            # 绘制车辆轮廓和ID
            cv2.rectangle(frame, rec, (0, 255, 0), 2)
            # 中心点
            # if y + h >= lineHigh:
            cv2.putText(
                frame, "Car", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )
            center = calcuCenter(rec)
            # 中心点
            cv2.circle(frame, center, 3, (0, 255, 0), -1)
            if (
                center[1] + offset >= lineHigh >= center[1] - offset
            ) and car_id not in tracked_cars:
                carCount += 1
                tracked_cars[car_id] = True

        cntmsg = f"Car count:{carCount}"
        cv2.putText(
            frame, cntmsg, (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2
        )
        cv2.imshow("Video", frame)
        # cv2.imshow("erode", erode)
        # cv2.imshow("dilate", dilate)
        # cv2.imshow("close", close)
        key = cv2.waitKey(25) & 0xFF
        if key == 10 or key == 13:  # Exit the loop if 'enter' is pressed
            break

    # print(tracked_cars)
    cap.release()  # Release the video capture object
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
