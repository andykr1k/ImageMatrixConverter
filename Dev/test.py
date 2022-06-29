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
r = 0
c =0
rowmax = img.shape[0] - 1
colmax = img.shape[1] - 1

#If Heirarchy for different pixel cases
if (r == 0 and c ==0): # Top Left Pixel
    #####################Average of quarter layer pixels (2x2)(Top Left)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.44445
    side = 0.22223
    diag = 0.11112

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
elif (r == 0 and c == colmax):  # Top Right Pixel
    #####################Average of quarter layer pixels (2x2)(Top Right)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.44445
    side = 0.22223
    diag = 0.11112

    #Middle
    redCounter = img[r][c][0]*middle + redCounter
    blueCounter = img[r][c][1]*middle + blueCounter
    greenCounter = img[r][c][2]*middle + greenCounter

    #Left
    redCounter = img[r-1][c][0]*side + redCounter
    blueCounter = img[r-1][c][1]*side + blueCounter
    greenCounter = img[r-1][c][2]*side + greenCounter

    #Bottom middle
    redCounter = img[r][c+1][0]*side + redCounter
    blueCounter = img[r][c+1][1]*side + blueCounter
    greenCounter = img[r][c+1][2]*side + greenCounter

    #Bottom left
    redCounter = img[r-1][c+1][0]*diag + redCounter
    blueCounter = img[r-1][c+1][1]*diag + blueCounter
    greenCounter = img[r-1][c+1][2]*diag + greenCounter

    redAvg = redCounter
    blueAvg = blueCounter
    greenAvg = greenCounter

    print("The average of the red pixels is:", redAvg)
    print("The average of the blue pixels is:", blueAvg)
    print("The average of the green pixels is:", greenAvg)
    #####################Average of quarter layer pixels (2x2)##########################
elif (r == rowmax and c == 0): # Bottom Left Pixel
    #####################Average of quarter layer pixels (2x2)(Bottom Left)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.44445
    side = 0.22223
    diag = 0.11112

    #Middle
    redCounter = img[r][c][0]*middle + redCounter
    blueCounter = img[r][c][1]*middle + blueCounter
    greenCounter = img[r][c][2]*middle + greenCounter

    #Right
    redCounter = img[r+1][c][0]*side + redCounter
    blueCounter = img[r+1][c][1]*side + blueCounter
    greenCounter = img[r+1][c][2]*side + greenCounter

    #Top middle
    redCounter = img[r][c-1][0]*side + redCounter
    blueCounter = img[r][c-1][1]*side + blueCounter
    greenCounter = img[r][c-1][2]*side + greenCounter

    #Top right
    redCounter = img[r+1][c-1][0]*diag + redCounter
    blueCounter = img[r+1][c-1][1]*diag + blueCounter
    greenCounter = img[r+1][c-1][2]*diag + greenCounter

    redAvg = redCounter
    blueAvg = blueCounter
    greenAvg = greenCounter

    print("The average of the red pixels is:", redAvg)
    print("The average of the blue pixels is:", blueAvg)
    print("The average of the green pixels is:", greenAvg)
    #####################Average of quarter layer pixels (2x2)##########################
elif (r == rowmax and c == colmax): # Bottom Right Pixel
    #####################Average of quarter layer pixels (2x2)(Bottom Right)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.44445
    side = 0.22223
    diag = 0.11112

    #Left
    redCounter = img[r-1][c][0]*side + redCounter
    blueCounter = img[r-1][c][1]*side + blueCounter
    greenCounter = img[r-1][c][2]*side + greenCounter

    #Middle
    redCounter = img[r][c][0]*middle + redCounter
    blueCounter = img[r][c][1]*middle + blueCounter
    greenCounter = img[r][c][2]*middle + greenCounter

    #Top left
    redCounter = img[r-1][c-1][0]*diag + redCounter
    blueCounter = img[r-1][c-1][1]*diag + blueCounter
    greenCounter = img[r-1][c-1][2]*diag + greenCounter

    #Top middle
    redCounter = img[r][c-1][0]*side + redCounter
    blueCounter = img[r][c-1][1]*side + blueCounter
    greenCounter = img[r][c-1][2]*side + greenCounter

    redAvg = redCounter
    blueAvg = blueCounter
    greenAvg = greenCounter

    print("The average of the red pixels is:", redAvg)
    print("The average of the blue pixels is:", blueAvg)
    print("The average of the green pixels is:", greenAvg)
    #####################Average of quarter layer pixels (2x2)##########################
elif (r == 0): # Top Row
    #####################Average of half layer pixels (2x3)(Top Row)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.33334
    side = 0.16667
    diag = 0.08334

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
elif (r == rowmax): # Bottom Row
    #####################Average of half layer pixels (2x3)(Bottom Row)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.33334
    side = 0.16667
    diag = 0.08334

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


    redAvg = redCounter
    blueAvg = blueCounter
    greenAvg = greenCounter

    print("The average of the red pixels is:", redAvg)
    print("The average of the blue pixels is:", blueAvg)
    print("The average of the green pixels is:", greenAvg)
    #####################Average of half layer pixels (2x3)##########################
elif (c == 0): # Left Column
    #####################Average of half layer pixels (2x3)(Left Coloumn)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.33334
    side = 0.16667
    diag = 0.08334

    #Middle
    redCounter = img[r][c][0]*middle + redCounter
    blueCounter = img[r][c][1]*middle + blueCounter
    greenCounter = img[r][c][2]*middle + greenCounter

    #Right
    redCounter = img[r+1][c][0]*side + redCounter
    blueCounter = img[r+1][c][1]*side + blueCounter
    greenCounter = img[r+1][c][2]*side + greenCounter


    #Top middle
    redCounter = img[r][c-1][0]*side + redCounter
    blueCounter = img[r][c-1][1]*side + blueCounter
    greenCounter = img[r][c-1][2]*side + greenCounter

    #Top right
    redCounter = img[r+1][c+1][0]*diag + redCounter
    blueCounter = img[r+1][c+1][1]*diag + blueCounter
    greenCounter = img[r+1][c+1][2]*diag + greenCounter

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
elif (c == colmax): # Right Column
    #####################Average of half layer pixels (2x3)(Right Coloumn)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.33334
    side = 0.16667
    diag = 0.08334

    #Middle
    redCounter = img[r][c][0]*middle + redCounter
    blueCounter = img[r][c][1]*middle + blueCounter
    greenCounter = img[r][c][2]*middle + greenCounter

    #Top left
    redCounter = img[r-1][c-1][0]*diag + redCounter
    blueCounter = img[r-1][c-1][1]*diag + blueCounter
    greenCounter = img[r-1][c-1][2]*diag + greenCounter

    #Top middle
    redCounter = img[r][c-1][0]*side + redCounter
    blueCounter = img[r][c-1][1]*side + blueCounter
    greenCounter = img[r][c-1][2]*side + greenCounter

    #Bottom middle
    redCounter = img[r][c+1][0]*side + redCounter
    blueCounter = img[r][c+1][1]*side + blueCounter
    greenCounter = img[r][c+1][2]*side + greenCounter

    #Bottom left
    redCounter = img[r-1][c+1][0]*diag + redCounter
    blueCounter = img[r-1][c+1][1]*diag + blueCounter
    greenCounter = img[r-1][c+1][2]*diag + greenCounter

    redAvg = redCounter
    blueAvg = blueCounter
    greenAvg = greenCounter

    print("The average of the red pixels is:", redAvg)
    print("The average of the blue pixels is:", blueAvg)
    print("The average of the green pixels is:", greenAvg)
    #####################Average of half layer pixels (2x3)##########################
else: # Middle Pixels
    #####################Average of full layer pixels (3x3)(Middle Pixels)##########################
    redCounter = 0
    blueCounter = 0
    greenCounter = 0
    middle = 0.25
    side = 0.125
    diag = 0.0625

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

#Converts AxesImage into Image and saves the new image
#converted = plt.imshow(img, interpolation='nearest')
#plt.savefig('converted.png', bbox_inches='tight', pad_inches=0)