import numpy as np
import cv2


def main():
    num = cv2.imread("data/imgs/ocr_numbers.png")
    num_gray = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
    # 二值化处理
    ret, num_thresh = cv2.threshold(
        num_gray, 10, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    # 轮廓检测
    contours, hierarchy = cv2.findContours(
        num_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 绘制轮廓
    cv2.drawContours(num, contours, -1, (0, 255, 0), 3)
    print(f" {len(contours)} contours detected")
    # 将数字的轮廓数据排序：根据每个数字的最大外接矩形的x坐标进行排序
    # print(f"before { contours[0][0][0] = }")
    contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
    # print(f"after { contours[0][0][0] = }")

    new_size = (57, 88)
    digits = {}
    for i, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        # print(f"contour {i= },{x= }, {y= }")
        # cv2.rectangle(num, (x, y), (x + w, y + h), (0, 0, 255), 3)
        roi = num_thresh[y : y + h, x : x + w]
        roi = cv2.resize(roi, new_size, interpolation=cv2.INTER_AREA)
        digits[i] = roi

    print(f"{digits[0].shape = }")

    # 处理信用卡图片
    card = cv2.imread("data/imgs/creditcard1.png")

    h, w = card.shape[:2]
    ratio = w / h
    width = 300
    height = int(width / ratio)
    print(f"{ratio= },{height= }")

    card = cv2.resize(card, (width, height))
    card_gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("card_gray", card_gray)

    # 顶帽操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    card_gray = cv2.morphologyEx(card_gray, cv2.MORPH_TOPHAT, kernel)

    # sobel算子
    card_sobelX = cv2.Sobel(card_gray, cv2.CV_64F, 1, 0, ksize=3)
    # sobelY = cv2.Sobel(card_gray, cv2.CV_64F, 0, 1, ksize=3)
    card_sobelX = cv2.convertScaleAbs(card_sobelX)
    # card_sobelY = cv2.convertScaleAbs(card_sobelY)
    # template_gray = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

    # 闭操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    card_sobelX_ = cv2.morphologyEx(card_sobelX, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("close", card_sobelX_)

    # 大津二值化
    ret, card_thresh = cv2.threshold(
        card_sobelX_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )
    # cv2.imshow("card_thresh", card_thresh)

    # 轮廓检测
    cardcontours, card_hierarchy = cv2.findContours(
        card_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 在原图上画出轮廓
    card_copy = card.copy()
    # cv2.drawContours(card_copy, cardcontours, -1, (0, 255, 0), 3)

    # 遍历轮廓，计算外接矩形，然后根据数字的长宽比找出真正的数字区域
    min_ratio = 3.15
    max_ratio = 3.5
    acc_areas = []
    for contour in cardcontours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # print(f"contour {i= },{x= }, {y= },{w= },{h= }")
        # 计算外接矩形的长宽比，相似的为数字区域，【1234  5678  2345  1234】
        aspectRatio = round(float(w / h), 4)
        # print(f"{aspectRatio = }")
        # t = str(aspectRatio)
        # ft = cv2.FONT_HERSHEY_SIMPLEX
        # !important 输出文字查看每个区域的大小比，得出[min_ratio= 3.15]与[max_ratio= 3.5]
        # cv2.putText(card_copy, t, (x, y - 5), ft, 0.6, (0, 0, 255), 2)

        # 筛选出合适的区域
        if aspectRatio > min_ratio and aspectRatio < max_ratio:
            # !根据实际图片大小，适当调整数字
            if (w > 40 and w < 55) and (h > 10 and h < 20):
                # 绘制矩形
                acc_areas.append((x, y, w, h))
                # cv2.rectangle(card_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 数字区域数组按照x坐标从左到右排序
    acc_areas = sorted(acc_areas, key=lambda x: x[0])
    print(f"{acc_areas = }")
    # 遍历轮廓，计算外接矩形，然后根据数字的长宽比找出真正的数字区域
    min_ratio = 0.4
    max_ratio = 0.8
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 255)
    for i, (gx, gy, gw, gh) in enumerate(acc_areas):
        # 从数字区域中提取数字, 并增加冗余空间
        roi_g = card_gray[gy - 5 : gy + gh + 5, gx - 5 : gx + gw + 5]
        # # 显示ROI_G
        # cv2.imshow("ROI_G", roi_g)
        # cv2.waitKey(0)
        # 二值化的作用：将灰度图像转换为二值图像，以便后续的轮廓检测和数字识别。
        ret_g, roi_g = cv2.threshold(roi_g, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # # 显示ROI_G
        # cv2.imshow("ROI_G threshold", roi_g)
        # cv2.waitKey(0)
        # 轮廓检测
        roi_g_contours, roi_g_hierarchy = cv2.findContours(
            roi_g, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        roi_g_contours = sorted(roi_g_contours, key=lambda x: cv2.boundingRect(x)[0])

        output_nums = []
        for contour in roi_g_contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            # print(f"{x= }, {y= }, {w= }, {h= }")
            # 找到数字的轮廓，提取数字区域
            roi = roi_g[y : y + h, x : x + w]
            # 调整大小
            roi = cv2.resize(roi, new_size)
            # # 显示ROI
            # cv2.imshow("ROI", roi)
            # cv2.waitKey(0)

            # 匹配数字
            scores = []
            for digit, digitROI in digits.items():
                result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF)
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)
            # 找到最大得分的数字
            ind = np.argmax(scores)
            # print(f"{ind= }")  # ind 即对应digits对应的数字
            output_nums.append(str(ind))
            # # 绘制结果

            # roi_pt = (gx + x - 10, gy + y - 10)
            # cv2.putText(card_copy, str(ind), roi_pt, font, 1, color, 2)

            # print(f"{scores= }")
        cv2.rectangle(card_copy, (gx - 5, gy - 5), (gx + gw + 5, gy + gh + 5), color, 2)
        cv2.putText(
            card_copy, "".join(output_nums), (gx - 10, gy - 10), font, 0.75, color, 2
        )

    cv2.imshow("card_copy", card_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
