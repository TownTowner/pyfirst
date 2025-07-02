import cv2
import numpy as np


def drawLines():
    img = cv2.imread("data/imgs/angles.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mouse(event, x, y, flags, param):
    img = param["img"]
    win = param["win"]
    # print(param)
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, y, cv2.FILLED)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        points.append((x, y))
        if len(points) == 3:
            p0, p1, p2 = points
            cv2.line(img, p0, p1, (0, 255, 0), 2)
            cv2.line(img, p0, p2, (0, 255, 0), 2)
            # 计算两条边的夹角
            angle = np.arctan2(p2[1] - p0[1], p2[0] - p0[0]) - np.arctan2(
                p1[1] - p0[1], p1[0] - p0[0]
            )
            angle = np.rad2deg(angle)
            if angle < 0:
                angle += 180
            print(angle)
            # 显示角度
            cv2.putText(img, str(round(angle, 2)), p0, fnt, 1, (0, 0, 255), 2)
            points.clear()
        # 刷新当前窗口
        cv2.imshow(win, img)


def calcuAngle():
    img = cv2.imread("data/imgs/angles.png")

    cv2.imshow("img", img)
    win = "img"
    cv2.setMouseCallback(win, mouse, {"img": img, "win": win})

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    points.clear()


points = []
fnt = cv2.FONT_HERSHEY_SIMPLEX


def main():
    # drawLines()
    calcuAngle()


if __name__ == "__main__":
    main()
