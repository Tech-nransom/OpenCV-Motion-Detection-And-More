import cv2


def click_event(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(str(x) + "," + str(y))
    if events == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(blue, green, red)


img = cv2.imread("marble_img.png", -1)
cv2.imshow("Display", img)
cv2.setMouseCallback("Display", click_event)
key_val = cv2.waitKey(0)
if key_val == 27:  # 27 Is For Escape Key

    cv2.destroyAllWindows()  # Closes The Image
elif key_val == ord("s"):  # If 's' is Pressed On The Keyboard The Do This
    cv2.imwrite("marble_img_cpy.png", img)  # Creates a Copy Of Image
    cv2.destroyAllWindows()
