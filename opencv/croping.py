import os 
import cv2

img = cv2.imread(os.path.join("img1.jpg"))

cv2.imshow('original image' , img)
cv2.waitKey()


print(img.shape)

newimage = img[0:1500 , 500:2500]

cv2.imshow("newImage", newimage)
cv2.waitKey()