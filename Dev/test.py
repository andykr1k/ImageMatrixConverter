from matplotlib import pyplot as plt
import matplotlib.image as image
import sys
import os

#Converts Image into AxesImage
img = image.imread("person.jpeg")

#Copy of Image for new matrix
img2 = img.copy()

#Intialize new matrix dimensions
rowmax = img2.shape[0] - 1
colmax = img2.shape[1] - 1

# Iterate through img1 and modify img2
for r in range(rowmax):
    for c in range(colmax):
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
            #####################Average of half layer pixels (2x3)##########################
        elif (r > 1 and c > 1 and r < rowmax - 1 and c < colmax - 1): # Second Layers
            #####################Average of two layer pixels (4x3)(Second Layer)##########################
            redCounter = 0
            blueCounter = 0
            greenCounter = 0
            middle = 0.25
            side = 0.11
            diag = 0.05
            second = 0.01

            #Top Top Middle Left // Second Layer
            redCounter = img[r-1][c-2][0]*second + redCounter
            blueCounter = img[r-1][c-2][1]*second + blueCounter
            greenCounter = img[r-1][c-2][2]*second + greenCounter
            #Top Top Middle Middle // Second Layer
            redCounter = img[r][c-2][0]*second + redCounter
            blueCounter = img[r][c-2][1]*second + blueCounter
            greenCounter = img[r][c-2][2]*second + greenCounter
            #Top Top Middle Right // Second Layer
            redCounter = img[r+1][c-2][0]*second + redCounter
            blueCounter = img[r+1][c-2][1]*second + blueCounter
            greenCounter = img[r+1][c-2][2]*second + greenCounter

            # Left Left Middle Up // Second Layer
            redCounter = img[r-2][c-1][0]*second + redCounter
            blueCounter = img[r-2][c-1][1]*second + blueCounter
            greenCounter = img[r-2][c-1][2]*second + greenCounter

            # Left Left Middle // Second Layer
            redCounter = img[r-2][c][0]*second + redCounter
            blueCounter = img[r-2][c][1]*second + blueCounter
            greenCounter = img[r-2][c][2]*second + greenCounter
            # Left Left Middle Down // Second Layer
            redCounter = img[r-2][c+1][0]*second + redCounter
            blueCounter = img[r-2][c+1][1]*second + blueCounter
            greenCounter = img[r-2][c+1][2]*second + greenCounter

            # Right Right Middle Up // Second Layer
            redCounter = img[r+2][c-1][0]*second + redCounter
            blueCounter = img[r+2][c-1][1]*second + blueCounter
            greenCounter = img[r+2][c-1][2]*second + greenCounter

            # Right Right Middle // Second Layer
            redCounter = img[r+2][c][0]*second + redCounter
            blueCounter = img[r+2][c][1]*second + blueCounter
            greenCounter = img[r+2][c][2]*second + greenCounter

            # Right Right Middle Down // Second Layer
            redCounter = img[r+2][c+1][0]*second + redCounter
            blueCounter = img[r+2][c+1][1]*second + blueCounter
            greenCounter = img[r+2][c+1][2]*second + greenCounter

            #Bottom Bottom Middle Left // Second Layer
            redCounter = img[r-1][c+2][0]*second + redCounter
            blueCounter = img[r-1][c+2][1]*second + blueCounter
            greenCounter = img[r-1][c+2][2]*second + greenCounter

            #Bottom Bottom Middle Middle // Second Layer
            redCounter = img[r][c+2][0]*second + redCounter
            blueCounter = img[r][c+2][1]*second + blueCounter
            greenCounter = img[r][c+2][2]*second + greenCounter

            #Bottom Bottom Middle Right // Second Layer
            redCounter = img[r+1][c+2][0]*second + redCounter
            blueCounter = img[r+1][c+2][1]*second + blueCounter
            greenCounter = img[r+1][c+2][2]*second + greenCounter

            #Bottom left // First Layer
            redCounter = img[r-1][c-1][0]*diag + redCounter
            blueCounter = img[r-1][c-1][1]*diag + blueCounter
            greenCounter = img[r-1][c-1][2]*diag + greenCounter

            #Top middle // First Layer
            redCounter = img[r][c-1][0]*side + redCounter
            blueCounter = img[r][c-1][1]*side + blueCounter
            greenCounter = img[r][c-1][2]*side + greenCounter

            #Top right // First Layer
            redCounter = img[r+1][c+1][0]*diag + redCounter
            blueCounter = img[r+1][c+1][1]*diag + blueCounter
            greenCounter = img[r+1][c+1][2]*diag + greenCounter

            #Left // First Layer
            redCounter = img[r-1][c][0]*side + redCounter
            blueCounter = img[r-1][c][1]*side + blueCounter
            greenCounter = img[r-1][c][2]*side + greenCounter

            #Middle
            redCounter = img[r][c][0]*middle + redCounter
            blueCounter = img[r][c][1]*middle + blueCounter
            greenCounter = img[r][c][2]*middle + greenCounter

            #Right // First Layer
            redCounter = img[r+1][c][0]*side + redCounter
            blueCounter = img[r+1][c][1]*side + blueCounter
            greenCounter = img[r+1][c][2]*side + greenCounter

            #Bottom left // First Layer
            redCounter = img[r-1][c+1][0]*diag + redCounter
            blueCounter = img[r-1][c+1][1]*diag + blueCounter
            greenCounter = img[r-1][c+1][2]*diag + greenCounter

            #Bottom middle // First Layer
            redCounter = img[r][c+1][0]*side + redCounter
            blueCounter = img[r][c+1][1]*side + blueCounter
            greenCounter = img[r][c+1][2]*side + greenCounter

            #Bottom right // First Layer
            redCounter = img[r+1][c+1][0]*diag + redCounter
            blueCounter = img[r+1][c+1][1]*diag + blueCounter
            greenCounter = img[r+1][c+1][2]*diag + greenCounter

            redAvg = redCounter
            blueAvg = blueCounter
            greenAvg = greenCounter

            img2[r][c] = [redAvg, blueAvg, greenAvg]
            #####################Average of two layer pixels (4x3)(Second Layer)##########################
        else: #First Layers
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

            img2[r][c] = [redAvg, blueAvg, greenAvg]
            #####################Average of full layer pixels (3x3)##########################

#Converts AxesImage into Image and saves the new image
converted = plt.imshow(img2, interpolation='nearest')
plt.savefig('Dev/test.png', bbox_inches='tight', pad_inches=0)