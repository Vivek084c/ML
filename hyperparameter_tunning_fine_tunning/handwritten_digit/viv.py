import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import cv2


x = cv2.imread("dataset/9/9/0.png")

cv2.imshow("image", x)
cv2.waitKey()