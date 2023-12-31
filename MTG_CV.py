import cv2 as cv
import pytesseract


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

# the below function is magic that is kinda shitty
def findText(inputImage, switch):
    output = ""

    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = 'Tesseract/tesseract.exe'

    # Read image from which text needs to be extracted
    img = cv.imread(inputImage)

    # Convert the image to gray scale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (20, 20))

    # Applying dilation on the threshold image
    dilation = cv.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # create a copy of the image
    im2 = img.copy()

    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("recognized.txt", "a")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        output = text[1:40]

        # Appending the text into file
        file.write(text)
        file.write("\n")

        # Close the file
        file.close

    if switch == 1:
        formatted_1 = '"' + output + '"'
        print(formatted_1)
        return formatted_1

    formatted = output.replace(' ', '+')

    print(formatted)
    return formatted

"""
    if switch == 1:
        formatted_1 = formatted.replace('\n', ' o:')
        print(formatted_1)
        return formatted_1
"""



