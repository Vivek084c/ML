import os
import cv2

img = cv2.imread(os.path.join("L8","whiteboard.png"))
print(img.shape )

#to draw a line
cv2.line(img, (100,150), (300, 450), (0, 255, 0), 3)
cv2.imshow("line image",img)

#to draw a rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), 5)
cv2.imshow("rectangle image",img)

#to draw a circle
cv2.circle(img, (500, 550), 15, (255, 0, 0), 10 )
cv2.imshow("circle image",img)

#to draw a text
cv2.putText(img, "hellow world", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
cv2.imshow("text image",img)

cv2.waitKey()