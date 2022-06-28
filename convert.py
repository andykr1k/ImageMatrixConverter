from matplotlib import pyplot as plt
import matplotlib.image as image
import sys
import os

#Input for Image Name
os.system("clear")
name = input("Which image do you want to convert? \n")

#Converts Image into AxesImage
img = image.imread(name)

#Prints Details of Image
print('The image as array is:', img)
print('The Shape of the image is:',img.shape)
print("The size of the array/matrix is:", img.size)

# img[rows][columns][color]

#Calculates Averages from AxesImage Matrix and Stores into a new AxesImage Matrix
print("The size of img[0] is : ", img[0].size, " The values of img[0] are: \n", img[0])
print("The size of img[0][0] is : ", img[0][0].size, " The values of img[0][0] are: ", img[0][0])
print("The size of img[0][0][0] is : ", img[0][0][0].size, " The values of img[0][0][0] are: ", img[0][0][0])

#Converts AxesImage into Image and saves the new image
#converted = plt.imshow(img, interpolation='nearest')
#plt.savefig('converted.png', bbox_inches='tight', pad_inches=0)