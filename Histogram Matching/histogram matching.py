import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import random
from tabulate import tabulate


def generate_specification(total,size,randomness = 5000):
    prob = np.random.randint(0,randomness,size)
    rnd_array = np.random.multinomial(total, prob / prob.sum(), size=1)[0]
    return np.array(rnd_array)

def generate_histogram(image):
    hist = [0] * 256

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            hist[image[i,j]]  += 1
    return(np.array(hist))

def tabulation(matrix , headers):
    print(tabulate(matrix,headers=headers,tablefmt='orgtbl'))


image = cv.imread('test.jpg',0)
L = 256
#histogram of the original image
original_histogram = generate_histogram(image)
original_image_prob = original_histogram *(1/(image.shape[0]*image.shape[1]))
original_cdf = np.cumsum(original_image_prob)
hk = np.round(original_cdf * 7)
hk = hk.astype(int)
tabulation(np.column_stack((np.arange(256),original_histogram,original_image_prob,original_cdf,hk)),['Intensity Value','# of pixels','Probability','(L-1)*Probability','hk'])
print()
print()

#Desired Specification
desired_histogram = generate_specification(image.shape[0] * image.shape[1] , 256 , 500)
desired_image_prob = desired_histogram *(1/(image.shape[0]*image.shape[1]))
desired_cdf = np.cumsum(desired_image_prob)
vk = np.round(desired_cdf * 7)
vk = vk.astype(int)
tabulation(np.column_stack((np.arange(256),desired_histogram,desired_image_prob,desired_cdf,vk)),['Intensity Value','# of pixels','Probability ','(L - 1) * Probability','vk'])
print()
print()

map=[]
for i in range(len(hk)):
    vk_ind=np.searchsorted(vk,hk[i])
    map.append(vk_ind)
output=image.copy()
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        output[i,j]=map[image[i,j]]

tabulation(np.column_stack((np.arange(256),hk,vk,map)),['Intensity Value','hk','vk','Mapping'])
print()
print()

output_histogram=generate_histogram(output)
output_image_prob=output_histogram/(image.shape[0]*image.shape[1])

tabulation(np.column_stack((np.arange(256),output_histogram,output_image_prob)),['Intensity value','# of pixels','Probability'])
print()
print()

cv.namedWindow('Actual Image')
cv.imshow('Actual Image',image)


cv.namedWindow('Output Image')
cv.imshow('Output Image',output)
cv.waitKey(0)
cv.destroyAllWindows()