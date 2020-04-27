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
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_b = np.array([93, 169, 0])
    u_b = np.array([122, 255, 255])

    mask = cv.inRange(hsv, l_b, u_b)
    #
    # l_h = cv.getTrackbarPos("l_h", "Tracker")
    # l_s = cv.getTrackbarPos("l_s", "Tracker")
    # l_v = cv.getTrackbarPos("l_v", "Tracker")
    #
    # u_h = cv.getTrackbarPos("u_h", "Tracker")
    # u_s = cv.getTrackbarPos("u_s", "Tracker")
    # u_v = cv.getTrackbarPos("u_v", "Tracker")

    # ret, thresh = cv.threshold(frame, 127, 255, 0)
    _, contors, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for con in contors:
        area = cv.contourArea(con)

        if (area > 1000):
            cv.drawContours(frame, contors, -1, (0, 255, 0), 2)

    k = cv.waitKey(1) & 0xff
    if k == 27:
        break

    # 0,131,137,255,255,255 - blue bottle

    cv.imshow("mask", mask)
    cv.imshow("Image", frame)

cap.release()
cv.destroyAllWindows()
