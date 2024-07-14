import cv2
import os

#reaing an image
image_path = os.path.join('.',"img1.jpg")
img = cv2.imread(image_path)

#writing an image file
cv2.imwrite(os.path.join('.',"img_out.jpg"), img)

#visualising an image
cv2.imshow("image file", img)
cv2.waitKey()