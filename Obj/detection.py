import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)

cv.namedWindow("Tracker")

cv.createTrackbar("l_h", "Tracker", 0, 255, nothing)
cv.createTrackbar("l_s", "Tracker", 0, 255, nothing)
cv.createTrackbar("l_v", "Tracker", 0, 255, nothing)
cv.createTrackbar("u_h", "Tracker", 255, 255, nothing)
cv.createTrackbar("u_s", "Tracker", 255, 255, nothing)
cv.createTrackbar("u_v", "Tracker", 255, 255, nothing)

while True:
    # img = cv.imread("marble_img.png")
    _, img = cap.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos("l_h", "Tracker")
    l_s = cv.getTrackbarPos("l_s", "Tracker")
    l_v = cv.getTrackbarPos("l_v", "Tracker")

    u_h = cv.getTrackbarPos("u_h", "Tracker")
    u_s = cv.getTrackbarPos("u_s", "Tracker")
    u_v = cv.getTrackbarPos("u_v", "Tracker")

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)
    #0,131,137,255,255,255 - blue bottle
    res = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("mask", mask)
    cv.imshow("res", res)
    cv.imshow("Image", hsv)

cap.release()
cv.destroyAllWindows()
