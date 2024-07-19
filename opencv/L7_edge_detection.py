import cv2
import os

img =  cv2.imread("bear.jpg")

cv2.imshow("original image", img)

edge = cv2.Canny(img, 180, 200)
cv2.imshow("edge_1", edge)

cv2.waitKey()