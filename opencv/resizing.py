import os 
import cv2

#reading the image file
img = cv2.imread("img1.jpg")

print(f"the shape of the image is {img.shape}")

#dispaying the original image file
cv2.imshow("original image file", img)
cv2.waitKey()

#to resize the orignal image file
newImaage = cv2.resize(img, (1492, 1415))

print("the shape of the new image file is ", newImaage.shape)
cv2.imshow("new image", newImaage)
cv2.waitKey()