import cv2
import numpy as np

img = cv2.imread('Friends season 7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.imread("chandler.jpg", 0)

w, h = temp.shape[::-1]
res = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)

# print(res)
threshold = 0.99
location = np.where(res >= threshold)


for pts in zip(*location[::-1]):
    cv2.rectangle(img, pts, (pts[0] + w, pts[1] + h), (0, 255, 0), 2)
    print(pts)
    cv2.putText(img, "Chandler", (pts[0], pts[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)


cv2.imshow("Ans", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
