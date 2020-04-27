import cv2
import numpy as np

#img = np.zeros([700, 700, 3], np.uint8)
img = cv2.imread("Friends season 7.jpg", -1)

cv2.line(img, (0, 0), (50, 50), (255, 0, 0), 2)
# cv2.arrowedLine(img, (50, 50), (100, 100), (0, 20, 21), 4)
cv2.rectangle(img, (50, 50), (100, 100), (200, 200, 201), 1)
cv2.circle(img, (200, 300), 15, (255, 255, 0), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Test-01", (150, 250), font, 3, (255, 255, 255), 4)
cv2.imshow("TP", img)
cv2.waitKey(0)
cv2.destroyAllWindows()