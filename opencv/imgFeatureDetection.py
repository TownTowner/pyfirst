import cv2
from cv2.typing import IndexParams, SearchParams
import numpy as np

# 三种算法对比
# SIFT最慢，准确率最高
# SURF速度比SIFT快些，准确率差些
# ORB速度最快，可以实时检测，准确率最差


def siftExec(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

    sift = cv2.SIFT_create()  # Create a SIFT object
    # kp = sift.detect(gray, None)
    # kp, des = sift.compute(gray, kp)
    # print(len(kp))

    # Detect keypoints and compute descriptors
    kp, des = sift.detectAndCompute(gray, None)
    # KeyPoint list, numpy.ndarray of shape (N,128)
    # print(kp)  # Print the number of keypoints detected

    res = cv2.drawKeypoints(gray, kp, None)  # Draw keypoints on the image
    return res, img, kp, des


def shitomasExec(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(
        gray, maxCorners=200, qualityLevel=0.01, minDistance=10
    )
    corners = np.int0(corners)  # Convert the corners to integers
    print(corners)  # Print the corners detected

    res = img.copy()  # Copy the image to draw on
    for i in corners:  # Draw circles at the corners
        x, y = i.ravel()
        cv2.circle(res, (x, y), 3, 255, -1)
    return res, img


def surfExec(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # not implemented in opencv-python
    surf = cv2.xfeatures2d.SURF_create()  # Create a SURF object
    # kp = surf.detect(gray, None)
    # kp, des = surf.compute(gray, kp)
    # print(len(kp))

    # Detect keypoints and compute descriptors
    kp, des = surf.detectAndCompute(gray, None)
    # KeyPoint list, numpy.ndarray of shape (N,128)
    # print(kp)  # Print the number of keypoints detected

    res = cv2.drawKeypoints(gray, kp, None)  # Draw keypoints on the image
    return res, img, kp, des


def orbExec(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()  # Create a ORB object
    # kp = orb.detect(gray, None)
    # kp, des = orb.compute(gray, kp)
    # print(len(kp))

    # Detect keypoints and compute descriptors
    kp, des = orb.detectAndCompute(gray, None)
    # KeyPoint list, numpy.ndarray of shape (N,128)
    print(des.shape)  # Print the number of keypoints detected

    res = cv2.drawKeypoints(gray, kp, None)  # Draw keypoints on the image
    return res, img, kp, des


def bfMatchExec(img1, img2):
    res1, img1, kp1, des1 = siftExec(img1)  # Compute descriptors for the first image
    res2, img2, kp2, des2 = siftExec(img2)  # Compute descriptors for the second image

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)  # Create a BFMatcher object
    matches = bf.match(des1, des2)  # Match descriptors
    # matches = sorted(matches, key=lambda x: x.distance)  # Sort matches by distance
    # Draw matches on the second image
    res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
    return res, img1, img2


def flannMatchExec(img1, img2):
    res1, img1, kp1, des1 = siftExec(img1)  # Compute descriptors for the first image
    res2, img2, kp2, des2 = siftExec(img2)  # Compute descriptors for the second image

    indexParams: IndexParams = {"algorithm": 0, "trees": 5}  # FLANN parameters
    # algorithm: 0 means using kdtree
    # trees: number of trees in the index,
    # checks: number of checks to perform, higher value means more accurate but slower
    # 根据经验，一般设置为50-100
    searchParams: SearchParams = {"checks": 50}

    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    # matches = flann.match(des1, des2)
    # res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)

    matches = flann.knnMatch(des1, des2, k=2)
    # print(matches)
    # 筛选匹配点,
    # Attention: 这里的k=2是指每个匹配点返回两个匹配点,所以matches是一个二维列表,
    #   每个元素是一个匹配点的列表,每个匹配点的列表有两个元素,分别是匹配点和距离
    matches = [[m for m, n in matches if m.distance < 0.7 * n.distance]]
    # print(matches)
    res = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None)
    return res, img1, img2


def picSearchExec(img1, img2):
    """单应性矩阵查找图片"""
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

    # 创建特征检测器和描述符
    sift = cv2.SIFT_create()  # Create a SIFT object
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # 根据经验，一般设置为50-100
    flann = cv2.FlannBasedMatcher(dict(algorithm=0, trees=5), dict(checks=50))
    matches = flann.knnMatch(des1, des2, k=2)
    # print(matches)
    matches = [[m for m, n in matches if m.distance < 0.7 * n.distance]]

    # 4是计算单应性矩阵的最小个数
    if len(matches[0]) < 4:
        print("匹配点数量不足4个")
        return None, None, None

    # 如果匹配点数量大于等于4,则认为匹配成功
    src_points = np.float32([kp1[m.queryIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
    # 计算单应性矩阵
    M, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
    h, w = img1.shape[:2]
    # 计算目标图像的四个角点
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    # 对图片进行透视变换
    # dst = cv2.warpPerspective(img2, M, (w, h), None, cv2.INTER_LINEAR)
    # 对矩阵进行透视变换
    dst = cv2.perspectiveTransform(pts, M)
    cv2.polylines(img2, [np.int32(dst)], True, (0, 0, 255), 3, cv2.LINE_AA)

    res = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None)
    return res, img1, img2


def picMergeExec(img1, img2):
    """图片拼接"""
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    matches = [[m for m, n in matches if m.distance < 0.7 * n.distance]]

    if len(matches[0]) < 4:
        print("匹配点数量不足4个")
        return None, None, None

    src_points = np.float32([kp1[m.queryIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
    # 计算单应性矩阵
    M, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    img1_pts = np.float32([[0, 0], [0, h1 - 1], [w1 - 1, h1 - 1], [w1 - 1, 0]]).reshape(
        -1, 1, 2
    )
    img2_pts = np.float32([[0, 0], [0, h2 - 1], [w2 - 1, h2 - 1], [w2 - 1, 0]]).reshape(
        -1, 1, 2
    )

    img1_pts_tran = cv2.perspectiveTransform(img1_pts, M)
    # 拼接
    pts = np.concatenate((img2_pts, img1_pts_tran), axis=0)
    # print(pts)
    # 对行聚合
    [xmin, ymin] = np.int32(pts.min(axis=0).ravel() - 1)
    [xmax, ymax] = np.int32(pts.max(axis=0).ravel() + 1)
    move_matrix = np.array([[1, 0, -xmin], [0, 1, -ymin], [0, 0, 1]])  # 平移矩阵
    # 对img1 进行平移透视变换
    result = cv2.warpPerspective(img1, move_matrix.dot(M), (xmax - xmin, ymax - ymin))
    # 如果不平移，直接使用透视变换，会出现拼接后的图片超出原始图片的范围
    # result = cv2.warpPerspective(img1, M, (xmax - xmin, ymax - ymin))
    # print(f"{result.shape = }")
    # print(f"{img1.shape = }")
    # print(f"{img2.shape = }")
    # print(f"{xmin = }, {ymin = }, {xmax = }, {ymax = }")
    # print(f"{h1 = }, {w1 = }, {h2 = }, {w2 = }")

    result[-ymin : h2 - ymin, -xmin : w2 - xmin] = img2
    return result, img1, img2


def getImg(picName, size=None):
    path = f"./data/imgs/{picName}"
    img = cv2.imread(path)
    if size is not None:
        img = cv2.resize(img, size)
    return (img, path)


def main():
    chess = "shudu.png"
    chess_sc = "shudu_sc.png"
    j = "j.png"
    j_480 = "j_480.png"
    j_dot = "j_dot.png"
    picMerge1 = "picMerge1.png"
    picMerge2 = "picMerge2.png"

    # result, img, *_ = siftExec(getImg(chess)[0])  # Execute SIFT on the image
    # result, img, *_ = shitomasExec(getImg(chess)[0])  # Execute Shi-Tomas on the image
    # result, img, *_ = surfExec(getImg(chess)[0])  # Execute SURF on the image
    # result, img, *_ = orbExec(getImg(chess)[0])  # Execute ORB on the image
    # cv2.imshow("result", np.hstack((img, result)))

    # result, img1, img2 = bfMatchExec(
    #     getImg(j)[0], getImg(j_480)[0]
    # )  # Execute BF on the images
    # result, img1, img2 = flannMatchExec(
    #     getImg(j)[0], getImg(j_480)[0]
    # )  # Execute FLANN on the images

    # result, img1, img2 = picSearchExec(
    #     getImg(j)[0], getImg(j_480)[0]
    # )  # Execute findHomogragh to search the images
    result, img1, img2 = picMergeExec(
        getImg(picMerge1, (640, 480))[0], getImg(picMerge2, (640, 480))[0]
    )

    if result is not None:
        cv2.imshow("result", result)
    else:
        print("no result")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
