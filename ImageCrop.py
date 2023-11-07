import matplotlib.pyplot as plt
import MTG_API
import MTG_CV
import cv2 as cv

def crop(inputImage):
    img = cv.imread(inputImage)
    try:
        print(img.shape)
    except:
        print("Please choose a file from the Test Images folder.")
    height = img.shape[0]
    width = img.shape[1]

    # Cut the image in half
    height_cutoff_top = round(height // 1.9)
    height_cutoff_top_extra = round(height // 9.25)
    height_cutoff_top_extra_extra = round(height // 20)

    width_cutoff_left = round(width // 6)
    width_cutoff_left_extra = round(width // 14)
    width_cutoff_right = round(width // 1.08)
    width_cutoff_right_extra = round(width // 1.3)

    height_cutoff_bottom = round(height // 1.6)

    s1 = img[height_cutoff_top_extra:height_cutoff_top, width_cutoff_left:width_cutoff_right]
    s2 = img[height_cutoff_bottom:, width_cutoff_left_extra:width_cutoff_right]
    s3 = img[height_cutoff_top_extra_extra:height_cutoff_top_extra, width_cutoff_left:width_cutoff_right_extra]
    s4 = img[height_cutoff_top_extra_extra:height_cutoff_top_extra, width_cutoff_left_extra:width_cutoff_right_extra]

    cv.imwrite("top.jpg", s1)
    cv.imwrite("bottom.jpg", s2)
    cv.imwrite("name.jpg", s3)
    cv.imwrite("fullname.jpg", s4)