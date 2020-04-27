import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
gray = cv2.cvtColor(apple,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
_, contors, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


print(len(contors))
print(contors[0])

cv2.drawContours(apple, contors, -1, (0, 255, 0), 2)

cv2.imshow("Apple", apple)

# cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
