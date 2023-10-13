import matplotlib.pyplot as plt
import MTG_API
import MTG_CV
import cv2 as cv

def crop(inputImage):
    img = cv.imread(inputImage)
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # Cut the image in half
    height_cutoff = round(height // 1.75)
    s1 = img[:height_cutoff, :]
    s2 = img[height_cutoff:, :]

    cv.imwrite("top.jpg", s1)
    cv.imwrite("bottom.jpg", s2)