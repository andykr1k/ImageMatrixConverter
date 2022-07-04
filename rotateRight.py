from matplotlib import pyplot as plt
import matplotlib.image as image
import sys
import os

#Converts Image into AxesImage
img = image.imread("Images/person.jpeg")

#Copy of Image for new matrix
img2 = img.copy()

#Intialize new matrix dimensions
rowmax = img2.shape[0] - 1
colmax = img2.shape[1] - 1

# Iterate Through Image Matrix and rotate right
for row in range(rowmax):
    for col in range(colmax):
        img2[row][colmax - col] = img[row][col]

#Converts AxesImage into Image and saves the new image
converted = plt.imshow(img2, interpolation='nearest')
plt.imsave("Converted/rotateRight.jpeg", img2)