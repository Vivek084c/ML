import cv2

#read webcam 
cam = cv2.VideoCapture(0)

#visualing the webcam
while True:
    ret, frame = cam.read()

    cv2.imshow('webcam window', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cam.release()
