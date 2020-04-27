import cv2

img = cv2.imread('baw.png', 0)
new_img = cv2.imread('trial.jpg')
ans = cv2.bitwise_not(new_img)
cv2.imshow("new_image", new_img)
# cv2.imshow("Orignal", img)
cv2.imshow("Answer", ans)
# cv2.imwrite("B&W_wallpaper.png", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
