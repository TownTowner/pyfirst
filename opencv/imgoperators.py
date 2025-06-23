from cv2.typing import MatLike
import numpy as np
import cv2


# 一阶求导
def sobelfilter(img) -> MatLike:
    dx = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)  # 对x方向求导
    dy = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)  # 对y方向求导
    cv2.imshow("sobel", np.hstack((dx, dy)))
    result = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)  # 加权求和
    # result = cv2.add(dx, dy)  # 求和
    return result


def scharrfilter(img) -> MatLike:
    # 只支持3*3的卷积核
    dx = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)  # 对x方向求导
    dy = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)  # 对y方向求导
    cv2.imshow("scharr", np.hstack((dx, dy)))
    result = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)  # 加权求和
    # result = cv2.add(dx, dy)  # 求和
    return result


def laplacianfilter(img) -> MatLike:
    result = cv2.Laplacian(img, -1, ksize=3)
    return result


def cannyfilter(img) -> MatLike:
    result = cv2.Canny(img, 100, 200)
    return result


def main():
    # 读取图像
    img = cv2.imread("./data/imgs/spongbob.png")
    lena = cv2.imread("./data/imgs/lena.png")
    shudu = cv2.imread("./data/imgs/shudu.png")

    # cv2.imshow("original", img)

    # result = sobelfilter(img)  # sobel滤波
    # result = scharrfilter(img)  # scharr滤波
    # result = laplacianfilter(shudu)  # 拉普拉斯滤波
    result = cannyfilter(lena)  # canny滤波
    # result = houghfilter(img)  # hough滤波
    # result = kmeansfilter(img)  # kmeans滤波
    # result = pcafilter(img)  # pca滤波
    # result = svdfilter(img)  # svd滤波
    # result = pca_svdfilter(img)  # pca_svd滤波
    # result = pca_svd_kmeansfilter(img)  # pca_svd_kmeans滤波
    # result = pca_svd_kmeans_houghfilter(img)  # pca_svd_kmeans_hough滤波
    # result = pca_svd_kmeans_hough_cannyfilter(img)  # pca_svd_kmeans_hough_canny滤波

    theone = None
    for i in [img, lena, shudu]:
        if np.array_equal(i.shape, result.shape):
            theone = i
            break
    cv2.imshow("result", (np.hstack((theone, result)) if theone else result))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
