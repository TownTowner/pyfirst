# OpenCV上有八种不同的目标追踪算法：
# BOOSTING Tracker：和Haarcascades（AdaBoost）背后所用的机器学习算法相同，但是距其诞生已有十多年
# 了。这一追踪器速度较慢，并且表现不好。（最低支持OpenCV3.0.0）
# MIL Tracker：比上一个追踪器更精确，但是失败率比较高。（最低支持OpenCV3.0.0）
# KCF Tracker：比BOOSTING和MIL都快，但是在有遮挡的情况下表现不佳。（最低支持OpenCV3.1.0）
# CSRT Tracker:比KCF稍精确，但速度不如后者。（最低支持OpenCV3.4.2）
# MedianFlow Tracker：出色的跟踪故障报告。当运动是可预测的并且没有遮挡时，效果非常好，但是对于快速跳
# 动或快速移动的物体，模型会失效。（最低支持OpenCV3.0.0）
# TLD Tracker：在多帧遮挡下效果最好。但是TLD的误报非常多，所以不推荐。（最低支持OpenCV3.0.0）
# MOSSE Tracker：速度真心快，但是不如CSRT和KCF的准确率那么高，如果追求速度选它准没错。（最低支持
# OpenCV 3.4.1）
# GOTURN Tracker：这是OpenCV中唯一一深度学习为基础的目标检测器。它需要额外的模型才能运行。（最低
# 支持OpenCV3.2.0）


def main():
    pass


if __name__ == "__main__":
    main()
