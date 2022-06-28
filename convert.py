from matplotlib import pyplot as plt
import matplotlib.image as image
import sys
import os

from numpy import average
from pyparsing import col

#Input for Image Name
os.system("clear")
name = input("Which image do you want to convert? \n")

#Converts Image into AxesImage
img = image.imread(name)

#Prints Details of Image
print('The image as array is:', img)
print('The Shape of the image is:',img.shape)
print("The size of the array/matrix is:", img.size)
print("The size of img[0] is : ", img[0].size, " The values of img[0] are: \n", img[0])
print("The size of img[0][0] is : ", img[0][0].size, " The values of img[0][0] are: ", img[0][0])
print("The size of img[0][0][0] is : ", img[0][0][0].size, " The values of img[0][0][0] are: ", img[0][0][0])
# img[rows][columns][color]

#Calculates Averages from AxesImage Matrix and Stores into a new AxesImage Matrix

#Dimensions of Image and Current Pixel
i = 0
j =0
rowmax = img.shape[0] - 1
colmax = img.shape[1] - 1

#If Heirarchy for different pixel cases
if (i == 0 and j ==0):
    something = 0
elif (i == 0 and j == colmax):
    something = 0
elif (i == rowmax and j == 0):
    something = 0
elif (i == rowmax and j == colmax):
    something = 0
elif (i == 0):
    something = 0
elif (i == rowmax):
    something = 0
elif (j == 0):
    something = 0
elif (j == colmax):
    something = 0
else:
    #Average of full layer pixels will go here
    something = 0

#Average of full layer pixels
redCounter = 0
blueCounter = 0
greenCounter = 0
middle = 0.25
side = 0.125
diag = 0.0625
r = 1
c = 1
#Top left
redCounter = img[r-1][c-1][0]*diag + redCounter
blueCounter = img[r-1][c-1][1]*diag + blueCounter
greenCounter = img[r-1][c-1][2]*diag + greenCounter

#Top middle
redCounter = img[r][c-1][0]*side + redCounter
blueCounter = img[r][c-1][1]*side + blueCounter
greenCounter = img[r][c-1][2]*side + greenCounter

#Top right
redCounter = img[r+1][c+1][0]*diag + redCounter
blueCounter = img[r+1][c+1][1]*diag + blueCounter
greenCounter = img[r+1][c+1][2]*diag + greenCounter

#Left
redCounter = img[r-1][c][0]*side + redCounter
blueCounter = img[r-1][c][1]*side + blueCounter
greenCounter = img[r-1][c][2]*side + greenCounter

#Middle
redCounter = img[r][c][0]*middle + redCounter
blueCounter = img[r][c][1]*middle + blueCounter
greenCounter = img[r][c][2]*middle + greenCounter

#Right
redCounter = img[r+1][c][0]*side + redCounter
blueCounter = img[r+1][c][1]*side + blueCounter
greenCounter = img[r+1][c][2]*side + greenCounter

#Bottom left
redCounter = img[r-1][c+1][0]*diag + redCounter
blueCounter = img[r-1][c+1][1]*diag + blueCounter
greenCounter = img[r-1][c+1][2]*diag + greenCounter

#Bottom middle
redCounter = img[r][c+1][0]*side + redCounter
blueCounter = img[r][c+1][1]*side + blueCounter
greenCounter = img[r][c+1][2]*side + greenCounter

#Bottom right
redCounter = img[r+1][c+1][0]*diag + redCounter
blueCounter = img[r+1][c+1][1]*diag + blueCounter
greenCounter = img[r+1][c+1][2]*diag + greenCounter

redAvg = redCounter
blueAvg = blueCounter
greenAvg = greenCounter

print("The average of the red pixels is:", redAvg)
print("The average of the blue pixels is:", blueAvg)
print("The average of the green pixels is:", greenAvg)

#Converts AxesImage into Image and saves the new image
#converted = plt.imshow(img, interpolation='nearest')
#plt.savefig('converted.png', bbox_inches='tight', pad_inches=0)