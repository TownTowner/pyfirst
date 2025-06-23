import cv2
from cv2.typing import MatLike
import numpy as np
from cvzone.HandTrackingModule import HandDetector


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        value,
        font=None,
        thickness=None,
        fill_color=None,
        text_color=None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.fill_color = fill_color or (225, 225, 225)
        self.text_color = text_color or (0, 0, 0)
        self.font = font or cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 2
        self.thickness = thickness or 2
        text_size = get_textsize(self.value, self.font, self.font_scale, self.thickness)
        self.text_offset_w = (self.width - text_size[0]) // 2
        self.text_offset_h = (self.height + text_size[1]) // 2

    def draw(self, img):
        f_sca = self.font_scale
        f_co = self.text_color
        f_th = self.thickness
        # 区域
        pt1 = (self.x, self.y)
        pt2 = (self.x + self.width, self.y + self.height)
        cv2.rectangle(img, pt1, pt2, self.fill_color, -1)
        cv2.rectangle(img, pt1, pt2, f_co, f_th)
        # 内容
        txt_pt = (self.x + self.text_offset_w, self.y + self.text_offset_h)
        cv2.putText(img, self.value, txt_pt, self.font, f_sca, f_co, f_th)

    def detect_click(self, img, pos):
        x, y = pos
        white = (225, 225, 225)
        green = (0, 255, 0)
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            pt1 = (self.x + 3, self.y + 3)
            pt2 = (self.x + self.width - 3, self.y + self.height - 3)

            cv2.rectangle(img, pt1, pt2, green, -1)
            txt_pt = (self.x + 25, self.y + 65)
            cv2.putText(img, self.value, txt_pt, self.font, 3, self.text_color, 3)
            return True
        return False


def get_button_list(
    x, y, font=None, fill_color=None, text_color=None
) -> (list[Button], list[list[str]]):
    thickness = 2
    width, height = 100, 100
    text_list = [
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", "/", ".", "="],
    ]
    button_list = []
    for j in range(len(text_list)):
        for i in range(len(text_list[j])):
            btn_x = x + width * i
            btn_y = y + height * j
            val = text_list[j][i]
            f_co = fill_color
            t_co = text_color
            btn = Button(btn_x, btn_y, width, height, val, font, thickness, f_co, t_co)
            button_list.append(btn)
    return button_list, text_list


def get_textsize(txt, font, scale, thickness):
    return cv2.getTextSize(txt, font, scale, thickness)[0]


def hand_click_detect(
    hand,
    detector: HandDetector,
    img: MatLike,
    button_list: list[Button],
    equation_text: str,
):
    lmList = hand["lmList"]
    # print(f"{hand["bbox"] = }, {hand["center"] = },{hand["type"] = }")
    # 取出食指和中指的点，计算两者的距离
    index_finger = (lmList[8][0], lmList[8][1])
    middle_finger = (lmList[12][0], lmList[12][1])
    # print(lmList)
    # print(index_finger)
    distance, _, img = detector.findDistance(index_finger, middle_finger, img)
    hit = False

    # 食指和中指的距离在一个阈值内，认为用户点击了按钮
    if distance >= 50:
        return hit, equation_text, img

    # print(f"{distance = }")

    # 遍历所有按钮，检查是否有按钮被点击
    for btn in button_list:
        if btn.detect_click(img, index_finger):
            hit = True
            print(f"用户点击了按钮：{btn.value}")
            if btn.value == "=":
                try:
                    output_text = str(eval(equation_text))
                except:
                    output_text = "Error"
                equation_text = output_text
            else:
                equation_text += btn.value
            break

    return hit, equation_text, img


def virtual_calculator():
    cam = cv2.VideoCapture(0)
    # 设置窗口大小
    cam.set(3, 1280)
    cam.set(4, 720)

    font = cv2.FONT_HERSHEY_PLAIN
    gray = (225, 225, 225)
    black = (0, 0, 0)
    button_start_x = 800
    button_start_y = 200

    # 输出区域边框
    output_start = (button_start_x, button_start_y - 100)
    output_end = (button_start_x + 400, button_start_y)
    button_list, button_text_list = get_button_list(
        button_start_x, button_start_y, font, gray, black
    )

    hand_detector = HandDetector(detectionCon=0.8, maxHands=1)
    equation_text = ""
    delay = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        # 左右反转
        frame = cv2.flip(frame, 1)
        # 检测手
        hands, frame = hand_detector.findHands(frame, flipType=False)
        # print(f"{hands = }")

        # 描绘计算器
        for btn in button_list:
            btn.draw(frame)

        # 输出框实心矩形
        cv2.rectangle(frame, output_start, output_end, gray, -1)
        # 输出框边框
        cv2.rectangle(frame, output_start, output_end, black, 2)

        if hands and delay == 0:
            # 检测手的位置
            hit, text, frame = hand_click_detect(
                hands[0], hand_detector, frame, button_list, equation_text
            )
            if hit:
                delay = 1
                equation_text = text

        if delay != 0:
            delay += 1
            if delay > 10:
                delay = 0

        # 假设点击了按钮后，需要将按钮的值显示在输出框中
        text_size = get_textsize(equation_text, font, 2, 2)
        text_w, text_h = text_size
        output_pt = (output_end[0] - text_w, output_end[1] - text_h)
        cv2.putText(frame, equation_text, output_pt, font, 2, black, 2)

        cv2.imshow("Virtual Calculator", frame)
        key = cv2.waitKey(10)
        if key == ord("q"):
            break
        elif key == ord("c"):
            equation_text = ""

    cam.release()
    cv2.destroyAllWindows()

    # 初始化虚拟计算器的显示区域
    calculator_area = np.zeros((400, 400, 3), dtype=np.uint8)
    cv2.imshow("Virtual Calculator", calculator_area)


def main():
    virtual_calculator()


if __name__ == "__main__":
    main()
