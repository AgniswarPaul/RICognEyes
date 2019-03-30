import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) #width=640
cap.set(4,480) #height=480

while True:
    b, img =cap.read()
    if b:
        cv2.imshow("Window",img)
        cv2.waitKey(1)
    else:
        break
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
cap.release()