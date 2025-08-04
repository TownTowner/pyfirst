import cv2
import cvzone
import numpy as np
import math
import random
from cvzone.HandTrackingModule import HandDetector


class Snake:
    def __init__(self, foodPath):
        self.score = 0
        self.gameOver = False

        self.points = []  # snake nodes
        self.lengths = []  # 每个节点的长度
        self.totalLength = 0  # 当前总长度
        self.allowedLength = 150  # 允许的最大长度
        self.prevHead = (0, 0)  # 上一个头节点
        self.direction = (0, 0)  # 方向

        self.imgFood = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = (0, 0)
        self.randomFoodLocation()

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, img, currentHead):
        prex, prey = self.prevHead
        curx, cury = currentHead

        distance = math.hypot(curx - prex, cury - prey)
        self.totalLength += distance
        self.lengths.append(distance)
        self.points.append(currentHead)
        self.prevHead = currentHead

        # 控制长度
        # print(f"{self.totalLength= },{distance= }")
        if self.totalLength > self.allowedLength:
            reduceIdx = 1
            for i in range(len(self.lengths)):
                length = self.lengths[i]
                self.totalLength -= length
                self.totalLength = self.totalLength if self.totalLength >= 0 else 0
                if self.totalLength <= self.allowedLength:
                    break
                reduceIdx = i + 1

            # print(f"{reduceIdx= },{self.lengths= }")
            self.lengths = self.lengths[reduceIdx:]
            # print(f"{reduceIdx= },{self.lengths= }")
            self.points = self.points[reduceIdx:]

        # check if eat the food
        rx, ry = self.foodPoint
        isXIn = rx - self.wFood // 2 < curx < rx + self.wFood // 2
        isYIn = ry - self.hFood // 2 < cury < ry + self.hFood // 2
        if isXIn and isYIn:
            self.randomFoodLocation()
            self.allowedLength += 50
            self.score += 1

        # draw snake
        if len(self.points) > 0:
            for i in range(1, len(self.points)):
                cv2.line(img, self.points[i - 1], self.points[i], (0, 255, 0), 20)
            cv2.circle(img, self.points[-1], 10, (255, 0, 0), cv2.FILLED)

        # draw food
        rx, ry = self.foodPoint
        rx, ry = rx - self.wFood // 2, ry - self.hFood // 2
        img = cvzone.overlayPNG(img, self.imgFood, (rx, ry))
        cvzone.putTextRect(img, f"Score: {self.score}", [50, 80])

        # Check for Collision
        # 不包含头部2个节点，因为头部2个节点会导致自碰撞。什么是自碰撞？
        # 自碰撞指的是蛇头与蛇身的碰撞。
        pts = np.array(self.points[:-2], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], False, (0, 255, 0), 3)
        minDist = cv2.pointPolygonTest(pts, (curx, cury), True)

        # 为什么是-1，与1之间？
        # 因为pointPolygonTest返回的是点到多边形的最短距离，
        # 如果点在多边形内部，返回值为-1。
        # 如果点在多边形外部，返回值为1。
        # 如果点在多边形边界上，返回值为0。
        # 不能直接用<1判断，这会错误地将距离多边形很远的外部点（例如 minDist = -100 ）也判定为"Hit"
        if -1 <= minDist <= 1:
            print("Hit")
            self.gameOver = True
            self.points = []  # all points of the snake
            self.lengths = []  # distance between each point
            self.totalLength = 0  # total length of the snake
            self.allowedLength = 150  # total allowed Length
            self.prevHead = 0, 0  # previous head point
            self.randomFoodLocation()

        return img


def main():
    # lst = [1, 2, 3]
    # for i in range(1, len(lst)):
    #     print(i)
    #     item = lst[i]
    #     print(i, item)
    # return

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    detector = HandDetector()
    snake = Snake("data/imgs/snake_food.png")

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            img = snake.update(img, lmList[8][0:2])
            # print(lmList)

        cv2.imshow("img", img)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
