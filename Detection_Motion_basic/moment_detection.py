import cv2
import numpy as np

cap = cv2.VideoCapture("vtest.avi")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

cv2.waitKey(0) & 0xff
while cap.isOpened():
    try:
        diff = cv2.absdiff(frame2, frame1)
    except (cv2.error):
        print("okay")
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None)
    _, contour, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, contour, -1, (0, 255, 0), 2)

    for con in contour:
        (x, y, w, h) = cv2.boundingRect(con)
        area = cv2.contourArea(con)

        if (area > 700):
            print(area)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Display", frame1)

    if cv2.waitKey(40) == 27:
        break
    frame1 = frame2
    ret, frame2 = cap.read()

cap.release()
cv2.destroyAllWindows()
