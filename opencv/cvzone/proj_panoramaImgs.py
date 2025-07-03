import cv2
import numpy as np
import os


def main():
    work_dir = "data/imgs/panorama/1/"
    work_dir = "data/imgs/panorama/2/"
    img_names = os.listdir(work_dir)
    print(img_names)
    stitcher = cv2.Stitcher().create()
    imgs = []
    for img_name in img_names:
        img = cv2.imread(work_dir + img_name)
        # (0,0)表示: 表示图片的高和宽分别乘以fx和fy
        img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
        imgs.append(img)
    # 拼接图片
    status, pano_img = stitcher.stitch(imgs)
    if status == cv2.STITCHER_OK:
        cv2.imshow("panorama", pano_img)
        # cv2.imwrite(f"{work_dir}panorama.jpg", pano_img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
