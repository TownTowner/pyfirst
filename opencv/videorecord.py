import cv2


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        exit()
    # *mp4v is the codec for mp4, equals to "M", "P", "4", "V"
    # xvid is the codec for avi, equals to "X", "V", "I", "D"
    fourcc = cv2.VideoWriter_fourcc(*"xvid")
    vw = cv2.VideoWriter("./data/record.mp4", fourcc, 30.0, (640, 480))
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break

        vw.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    vw.release()  # release the video writer
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
