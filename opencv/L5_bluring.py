import os
import cv2

# img = cv2.imread("img1.jpg")

# cv2.imshow("orignal image",img)

# kernal_size = 7

# img_blur = cv2.blur(img,(kernal_size, kernal_size))
# cv2.imshow("blur image", img_blur)

# img_gaussian_blur = cv2.GaussianBlur(img, (kernal_size, kernal_size), 3)
# cv2.imshow("guassian blur", img_gaussian_blur)

# img_mediam_blur = cv2.medianBlur(img, kernal_size)
# cv2.imshow("medium blur", img_mediam_blur)
# cv2.waitKey()

#to apply blur to remove noise
img_2 = cv2.imread("cow-salt-peper.png")
cv2.imshow("original_image", img_2)

k = 7
img_blur = cv2.blur(img_2, (k,k))
cv2.imshow("img_blur", img_blur)

img_guassian = cv2.GaussianBlur(img_2, (k, k), 3)
cv2.imshow("img_gussian", img_guassian)

img_median = cv2.medianBlur(img_2, k)
cv2.imshow("img_median", img_median)
cv2.waitKey()