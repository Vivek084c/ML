import os
import cv2

img = cv2.imread('bear.jpg')
cv2.imshow("original_image", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", img_gray)

ret , img_thrshold = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
cv2.imshow("threshold", img_thrshold)

img_threshold_2 = cv2.blur(img_thrshold, (10, 10))
cv2.imshow("blur_threohold", img_threshold_2)


ret , img_thrshold_3 = cv2.threshold(img_threshold_2, 80, 255, cv2.THRESH_BINARY)
cv2.imshow("threhoodl_3", img_thrshold_3)

cv2.waitKey()