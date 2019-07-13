import cv2
import converter

# Import picture & create HSI copy using algorithm
img = cv2.imread('11.JPG', 1)
hsi = converter.RGB_TO_HSI(img)

# Display HSV Image
cv2.imshow('HSI Image', hsi)

# The three value channels
cv2.imshow('H Channel', hsi[:, :, 0])
cv2.imshow('S Channel', hsi[:, :, 1])
cv2.imshow('I Channel', hsi[:, :, 2])

# Wait for a key press and then terminate the program
cv2.waitKey(0)
cv2.destroyAllWindows()

# Algorithm to convert RGB TO HSI :

#1.    Read a RGB image using ‘imread’ function.
#2.    Each RGB component will be in the range of [0 255].  Represent the image in [0 1] range by dividing the image by 255.
#3.    Find the theta value. If B<=G then H= theta. If B>G then H= 360-theta
#4.    Use ‘acosd’ function to find inverse cosine and obtain the result in degrees.
#5.    Divide the hue component by 360 to represent in the range [0 1]
#6.    Similarly, find the saturation and the intensity components.
#7.    Display the image.