import cv2
import numpy as np

img = cv2.imread('13.png',0)
hari1998


kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
row, column = img.shape
img1 = np.zeros((row, column), dtype='uint8')
for i in range(row):
    for j in range(column):
        img1[i,j] = img[i,j] - erosion[i,j]

cv2.imshow('Original_image',img)
cv2.imshow('erosion', erosion)

cv2.imshow('Boundary', img1)
cv2.waitKey(0)