import matplotlib.image as image
import sys
import os

os.system("clear")

name = input("Which image do you want to convert? \n")

img = image.imread(name)

print('The Shape of the image is:',img.shape)
print('The image as array is:', img)
print("The size of the array/matrix is:", img.size)