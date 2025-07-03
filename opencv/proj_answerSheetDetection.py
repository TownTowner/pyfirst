import cv2
import numpy as np


def main():
    img = cv2.imread("data/imgs/answersheet.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 去噪点
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # 答题卡四周边缘检测
    edged = cv2.Canny(gray, 75, 200)

    img_cp = img.copy()
    cnts, hierarchy = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 轮廓排序
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        # 计算周长
        peri = cv2.arcLength(c, True)
        # 多边形逼近
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    cv2.drawContours(img_cp, [screenCnt], -1, (0, 255, 0), 2)
    # 透视变换
    # 获得对应点坐标
    pts = screenCnt.reshape(4, 2)
    # print(f"{pts = }")
    # 按顺序左上、右上、右下、左下
    rect = np.zeros((4, 2), dtype="float32")
    # 计算左上、右下
    s = pts.sum(axis=1)
    # print(f"{s = }")
    # 左上的坐标一定是x+y最小的坐标，右下的坐标一定是x+y最大的坐标
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # 右上的坐标一定是y-x最小的坐标，左下的坐标一定是y-x最大的坐标
    diff = np.diff(pts, axis=1)  # diff, 后列-前列
    # print(f"{diff = }")
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # print(f"{rect = }")
    # 目标坐标
    (tl, tr, br, bl) = rect
    # 计算上下边宽度
    topWidth = np.sqrt((tl[0] - tr[0]) ** 2 + (tl[1] - tr[1]) ** 2)
    bottomWidth = np.sqrt((bl[0] - br[0]) ** 2 + (bl[1] - br[1]) ** 2)
    # 取较大值作为新的宽度
    maxWidth = max(int(topWidth), int(bottomWidth))
    # 计算左右边高度
    leftHeight = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    rightHeight = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    # 取较大值作为新的高度
    maxHeight = max(int(leftHeight), int(rightHeight))
    # 变换后坐标
    dst = np.array(
        [[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]],
        dtype="float32",
    )
    # 变换矩阵
    M = cv2.getPerspectiveTransform(rect, dst)
    # 透视变换
    warped = cv2.warpPerspective(gray, M, (maxWidth, maxHeight))
    # 二值化处理
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # 找轮廓
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(warped, cnts[0], -1, (0, 255, 0), 2) # test
    # print(cnts[0])
    # 排序；
    # - 如果返回结果长度为2（OpenCV 2.x格式），取第一个元素 cnts[0] （轮廓列表）
    # - 否则取第二个元素 cnts[1] （OpenCV 3.x格式中的轮廓列表）
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    # print(cnts[0])
    # 从上到下排序(根据y坐标排序)，使之依次为题目顺序
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    question_cnts = []
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)  # ar是宽高比
        # 筛选条件
        if w > 20 and h > 20 and ar > 0.6 and ar < 1.1:
            question_cnts.append(c)

    question_num = 5
    ans_num = 5
    question_score = 1
    score = question_num * question_score
    Answer_Keys = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}  # 正确答案

    if question_num * ans_num != len(question_cnts):
        raise Exception("检测到的轮廓数量与题目数量不匹配")

    blue = (255, 0, 0)
    green = (0, 255, 0)
    red = (0, 0, 255)
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    question_cnts = sorted(question_cnts, key=lambda c: cv2.boundingRect(c)[1])
    warpedColored = cv2.cvtColor(warped, cv2.COLOR_GRAY2BGR)
    for i in range(question_num):
        print(f"{i= }")
        cur_cnts = question_cnts[i * ans_num : (i + 1) * ans_num]
        # 从左到右排序(根据x坐标排序)，使之依次为选项顺序
        cur_cnts = sorted(cur_cnts, key=lambda c: cv2.boundingRect(c)[0])
        # print(f"{cur_cnts= }")

        q_hit = {"total": -1, "key": -1}
        for ci, c in enumerate(cur_cnts):
            (x, y, w, h) = cv2.boundingRect(c)
            txt = str(i * ans_num + ci)
            print(f"{txt= },{x= },{y= }")

            # cv2.rectangle(img_cp, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.putText(img_cp, txt, (x, y - 5), fnt, 0.5, (0, 255, 0), 2)
            # 提取选项
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            # 计算非零像素点的数量（即白色像素点的数量）,选中涂抹的答案为全白,白色像素最多
            total_pixels = cv2.countNonZero(mask)
            # 阈值判断
            if q_hit["key"] < 0 or total_pixels > q_hit["total"]:
                q_hit["total"] = total_pixels
                q_hit["key"] = ci

            # print(f"{total_pixels= }")
            # # 显示结果
            # cv2.imshow("Mask", mask)
            # cv2.waitKey(0)
        q_key = Answer_Keys[i]
        if q_key != q_hit["key"]:
            score -= question_score
            cv2.drawContours(warpedColored, [cur_cnts[q_hit["key"]]], -1, red, 2)
        cv2.drawContours(warpedColored, [cur_cnts[q_key]], -1, green, 2)
        # print(f'{txt= },{cur_cnts[q_hit["key"]] = }')

    cv2.putText(warpedColored, f"score:{score}", (10, 30), fnt, 0.9, blue, 2)
    cv2.imshow("warpedColored", warpedColored)
    # cv2.imshow("img", img_cp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
