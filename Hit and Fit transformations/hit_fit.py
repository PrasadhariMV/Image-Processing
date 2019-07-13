import cv2 as cv
import numpy as np

path="/home/prajwal/prajwal/opencv/tree.png"
img=cv.imread(path,0)

cv.namedWindow("Original Image")
cv.namedWindow("Fit Image")
cv.namedWindow("Hit Image")
cv.imshow('Original Image',img)

#Original image has pixel values of either 0 or 255.(Just two values)

img=img/255         #Binary Image, i.e. each pixel is either a zero or one
img=1-img           #Negate the image for easier calculation. Later negate the computed values
img=img.astype(int)



se=np.array([[0,1,0],[1,1,1],[0,1,0]]) #A structuing element of the form PLUS symbol (+)


m=se.shape[0]
a=int(m/2)
n=se.shape[0]
b=int(n/2)

img1=np.zeros((img.shape[0]+2,img.shape[1]+2))
img1[1:img.shape[0]+1,1:img.shape[1]+1]=img.copy()  #image with zeros padded
img2=np.zeros((img.shape[0]+2,img.shape[1]+2))      #image to be processed as FIT image
img3=np.zeros((img.shape[0]+2,img.shape[1]+2))      #image to be processed as HIT image
img1=img1.astype(int)

for i in range(1,img.shape[0]+1):
    for j in range(1,img.shape[1]+1):
            sum=0
            for l in range(-a, a + 1):
                for k in range(-b , b + 1):
                    sum = sum + se[l + 1][k + 1] * img1[i + l][j + k]   #Finding the sum of corresponding products

            if sum==5:        #Maximum sum possible since there are only five 1s in the filter
                img2[i][j]=1
            else:
                img2[i][j]=0
            if sum>0:
                img3[i][j]=1
            else:
                img3[i][j]=0

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        if img2[i][j]==1:     #Compensation of the initial negation of the image.
            img2[i][j]=0
        else:
            img2[i][j]=255
        if img3[i][j]==1:
            img3[i][j]=0
        else:
            img3[i][j]=255


cv.imshow('Fit Image',img2)
cv.imshow('Hit Image',img3)
cv.waitKey(0)
cv.destroyAllWindows()
