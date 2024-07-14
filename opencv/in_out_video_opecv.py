import cv2
import os

#reading the video file 
video_path = os.path.join(".","parking_crop.mp4")
vid = cv2.VideoCapture(video_path)

#visualsing the video
ret = True
while ret:
    #we get two variable, first the bool data and then the frame of the image
    ret , frame = vid.read()

    if ret:
        cv2.imshow("frame window", frame)
        cv2.waitKey(33)

#releasing the memory allocated for video and closing the window
vid.release()
cv2.destroyAllWindows()

