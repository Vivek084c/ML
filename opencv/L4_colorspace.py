import os
import cv2

img = cv2.imread("img1.jpg")

cv2.imshow("original image", img)


# chaing the color space of image
newImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("image_rbg", newImage)


#chaing to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_scale_image", img_gray)

#changing to hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv color space", img_hsv)
cv2.waitKey()