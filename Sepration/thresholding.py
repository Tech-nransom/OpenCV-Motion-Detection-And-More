import cv2
from matplotlib import pyplot as py

img = cv2.imread("gradient.jpg", 0)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_OTSU)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
_, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th7 = cv2.threshold(img, 50, 255, cv2.THRESH_TRIANGLE)
_, th8 = cv2.threshold(img, 50, 255, cv2.THRESH_MASK)

titles = ["Orignal", "Binary", "Otsu", "BInv", "Tozero", "TozINV", "Trunc", "Triangle", "Mask"]
images = [img, th1, th2, th3, th4, th5, th6, th7, th8]

for i in range(len(titles)):
    py.subplot(3, 3, i+1), py.imshow(images[i], "gray")
    py.title(titles[i])
    py.xticks([]), py.yticks([])

py.show()
