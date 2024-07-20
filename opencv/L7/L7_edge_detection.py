import cv2
import os
import numpy as np

img =  cv2.imread("bear.jpg")

cv2.imshow("original image", img)

edge = cv2.Canny(img, 180, 200)
cv2.imshow("edge_1", edge)

#below code makes like the edge draw a line or draw line on the border
img_edge_dilate = cv2.dilate(edge,np.ones((3, 3), dtype=np.int8) )
cv2.imshow("img_edge_dilate",img_edge_dilate)

img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3, 3), dtype=np.int8))
cv2.imshow("img_edge_erode", img_edge_erode)

cv2.waitKey()