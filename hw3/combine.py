import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
import configs
import utils


def main():
    img1 = utils.load_image(configs.img_1,gray=True)
    img2 = utils.load_image(configs.img_2,gray=True)

    #img2 = utils.transform(img1)

    # 实例化
    sift = cv2.SIFT_create()

    # 计算关键点和描述子
    # 其中kp为关键点keypoints
    # des为描述子descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # 绘出关键点
    # 其中参数分别是源图像、关键点、输出图像、显示颜色
    img3 = cv2.drawKeypoints(img1, kp1, img1, color=(0, 255, 255))
    img4 = cv2.drawKeypoints(img2, kp2, img2, color=(0, 255, 255))

    # 参数设计和实例化
    index_params = dict(algorithm=1, trees=6)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # 利用knn计算两个描述子的匹配
    res=[]
    matche = flann.knnMatch(des1, des2, k=2)
    for i, (m, n) in enumerate(matche):
        if (m.distance < 0.75 * n.distance):
            res.append(m)
    src_pts = np.float32([kp1[m.queryIdx].pt for m in res]).reshape(-1, 1, 2)
    ano_pts = np.float32([kp2[m.trainIdx].pt for m in res]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, ano_pts, cv2.RANSAC, 5.0)
    print(M)
    # 绘出匹配效果
    warpImg = cv2.warpPerspective(img2, np.linalg.inv(M), (img1.shape[1] + img2.shape[1], img2.shape[0]))
    #img5 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matche, None, flags=2)
    #combine = np.hstack((img1, warpImg))
    combine=np.hstack((img1,img2))
    '''
    cv2.imshow("KeyPoints", combine)
    cv2.waitKey(0)
    cv2.waitKey(0)
    '''
    #plt.imshow(warpImg,cmap='gray')
    plt.imshow(combine,cmap='gray')
    plt.show()

if __name__ == '__main__':
    main()