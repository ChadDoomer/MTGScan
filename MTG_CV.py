import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft

def compare(localIMG, searchIMG):
    img1 = cv.imread(localIMG, cv.IMREAD_GRAYSCALE)  # queryImage
    img2 = cv.imread(searchIMG, cv.IMREAD_GRAYSCALE)  # trainImage

    #  convert images to 8bit
    image8bit1 = cv.normalize(img1, None, 0, 255, cv.NORM_MINMAX).astype('uint8')
    image8bit2 = cv.normalize(img2, None, 0, 255, cv.NORM_MINMAX).astype('uint8')

    # Initiate SIFT detector
    sift = cv.SIFT.create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(image8bit1, None)
    kp2, des2 = sift.detectAndCompute(image8bit2, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # number of times the trees in the index should be recursively traversed
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Returns a value where higher means a better match
    matchCheck = [m[0] for m in matches if len(m) == 2 and m[0].distance < m[1].distance * 0.75]

    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]

    # ratio test
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]

    draw_params = dict(matchColor=(0, 0, 255),
                       singlePointColor=(0, 255, 0),
                       matchesMask=matchesMask,
                       flags=cv.DrawMatchesFlags_DEFAULT)

    img3 = cv.drawMatchesKnn(image8bit1, kp1, image8bit2, kp2, matches, None, **draw_params)
    # print(matchesMask)
    return len(matchCheck)

    # plt.imshow(img3, ), plt.show()
