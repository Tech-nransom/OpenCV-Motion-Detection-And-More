import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(3))  # 3 == cv2.CAP_PROP_FRAME_WIDTH
print(cap.get(4))  # 4 == cv2.CAP_PROP_FRAME_HIGHT
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("output.avi", fourcc, 20.0,(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        date_show = str(datetime.datetime.now())
        font = cv2.FONT_ITALIC
        frame = cv2.putText(frame, date_show, (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Checking", frame)

        # out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
