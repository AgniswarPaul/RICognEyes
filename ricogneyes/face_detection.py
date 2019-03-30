import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) #width=640
cap.set(4,480) #height=480
print("Video Input")
while True:
    b, img =cap.read()
    print("Reading input")
    if b:
        print("Output")
        cv2.imshow("Window",img)
        cv2.waitKey(1)