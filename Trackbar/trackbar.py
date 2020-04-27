import numpy as np
import cv2 as cv


def nothing(x):
    pass


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Image")

cv.createTrackbar("B", "Image", 0, 255, nothing)
cv.createTrackbar("G", "Image", 0, 255, nothing)
cv.createTrackbar("R", "Image", 0, 255, nothing)

while True:
    cv.imshow("Image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

    b = cv.getTrackbarPos("B", "Image")
    g = cv.getTrackbarPos("G", "Image")
    r = cv.getTrackbarPos("R", "Image")

    img[:] = [b, g, r]

cv.destroyAllWindows()

