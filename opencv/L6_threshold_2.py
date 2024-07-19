import os
import cv2

img = cv2.imread("handwritten.png")
cv2.imshow("original image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image", gray_img)

# ret,thresh = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow("image_thresh" , thresh)

thresh = cv2.adaptiveThreshold(gray_img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
cv2.imshow("adaptive threhold", thresh)

cv2.waitKey()