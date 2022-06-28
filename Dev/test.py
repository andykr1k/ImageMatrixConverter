from matplotlib import pyplot as plt
import matplotlib.image as image
import sys
import os

#Converts Image into AxesImage
img = image.imread("stock.jpeg")

#Prints Details of Image
print('The image as array is:', img)
print('The Shape of the image is:',img.shape)
print("The size of the array/matrix is:", img.size)
print("The size of img[0] is : ", img[0].size, " The values of img[0] are: \n", img[0])
print("The size of img[0][0] is : ", img[0][0].size, " The values of img[0][0] are: ", img[0][0])
print("The size of img[0][0][0] is : ", img[0][0][0].size, " The values of img[0][0][0] are: ", img[0][0][0])
# img[rows][columns][0 - red // 1 - blue // 2 - green]

#Calculates Averages from AxesImage Matrix and Stores into a new AxesImage Matrix

#Dimensions of Image and Current Pixel
i = 0
j =0
rowmax = img.shape[0] - 1
colmax = img.shape[1] - 1

#If Heirarchy for different pixel cases
if (i == 0 and j ==0):
    # Top Left Pixel
    something = 0
elif (i == 0 and j == colmax):
    # Top Right Pixel
    something = 0
elif (i == rowmax and j == 0):
    # Bottom Left Pixel
    something = 0
elif (i == rowmax and j == colmax):
    # Bottom Right Pixel
    something = 0
elif (i == 0):
    # Top Row
    something = 0
elif (i == rowmax):
    # Bottom Row
    something = 0
elif (j == 0):
    # Left Column
    something = 0
elif (j == colmax):
    # Right Column
    something = 0
else:
    # Middle Pixels
    something = 0

#####################Average of full layer pixels (3x3)(Middle Pixels)##########################
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
#####################Average of full layer pixels (3x3)##########################


#####################Average of half layer pixels (2x3)(Top Row)##########################
redCounter = 0
blueCounter = 0
greenCounter = 0
middle = 0.33334
side = 0.16667
diag = 0.08334
r = 0
c = 1
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
#####################Average of half layer pixels (2x3)##########################


#####################Average of quarter layer pixels (2x2)(Top Left)##########################
redCounter = 0
blueCounter = 0
greenCounter = 0
middle = 0.44445
side = 0.22223
diag = 0.11112
r = 0
c = 0

#Middle
redCounter = img[r][c][0]*middle + redCounter
blueCounter = img[r][c][1]*middle + blueCounter
greenCounter = img[r][c][2]*middle + greenCounter

#Right
redCounter = img[r+1][c][0]*side + redCounter
blueCounter = img[r+1][c][1]*side + blueCounter
greenCounter = img[r+1][c][2]*side + greenCounter

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
#####################Average of quarter layer pixels (2x2)##########################