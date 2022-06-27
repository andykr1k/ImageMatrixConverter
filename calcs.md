# Gaussian Blur Calculations

Find columns = w
Find rows = h
Find size = w * h

Iterate through matrix using row/column and size
Check how many pixels surround the current pixel
Calculate average using correct weights(distance and postion from current pixel) and the amount of pixels surrounding
Push average to new AxesImage Matrix