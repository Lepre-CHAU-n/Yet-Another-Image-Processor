# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Chau Pham and Aeon Seva
# Date: Nov 20, 2021
# Student Number: 301467436 and 301458995
# Description: 
# cmpt120imageManip.py 
# - I got help from classmates for the double/half sizing and the fish location
# This line has exactly 100 characters (including the period), use it to keep each line under limit.

# Imports file
import cmpt120imageProjHelper
import numpy
import copy 

# Manipulation Options

# Apply Red Filter
def redFilter(pixels):
  # Height and width of image
  height = len(pixels)
  width = len(pixels[0])
  # Gets a new black image to generate a new image everytime 
  black = cmpt120imageProjHelper.getBlackImage(width,height)
  for row in range(height):
    for col in range(width):
      # Sets blue and green to zero and red as original state
      r = pixels[row][col][0]
      g = pixels[row][col][1] 
      b = pixels[row][col][2]
      g = 0
      b = 0
      black[row][col] = (r,g,b)
  return black
  
# Apply Green Filter
def greenFilter(pixels):
  # Height and width of image
  height = len(pixels)
  width = len(pixels[0])
  # Gets a new black image to generate a new image everytime 
  black = cmpt120imageProjHelper.getBlackImage(width,height)
  for row in range(height):
    for col in range(width):
      # Sets blue and red to zero and green as original state
      r = pixels[row][col][0] 
      g = pixels[row][col][1]
      b = pixels[row][col][2] 
      r = 0
      b = 0
      black[row][col] = (r,g,b)

  return black

# Apply Blue Filter
def blueFilter(pixels):
  # Height and width of image 
  height = len(pixels)
  width = len(pixels[0])
  # Gets a new black image to generate a new image everytime 
  black = cmpt120imageProjHelper.getBlackImage(width,height)
  for row in range(height):
    for col in range(width):
      # Sets red and green to zero and blue as original state
      r = pixels[row][col][0] 
      g = pixels[row][col][1] 
      b = pixels[row][col][2]
      r = 0
      g = 0
      black[row][col] = (r,g,b)

  return black

# Apply Sepia Filter
def sepiaFilter(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])
    
    # Creating canvas (black img) to put newly created image on
    canvas = cmpt120imageProjHelper.getBlackImage(width, height)

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # Red, Blue, & Green colours of accessed pixel
            r = pixels[row][col][0]
            g = pixels[row][col][1]
            b = pixels[row][col][2]

        # Sepia Colour = weighted average of the original R/G/B values using formula
            # NOTE: floats turned to integers
            sepiaRed = int((r * .393) + (g *.769) + (b * .189))
            sepiaGreen = int((r * .349) + (g *.686) + (b * .168))
            sepiaBlue = int((r * .272) + (g *.534) + (b * .131))

        # Creating Sepia Pixel: placing sepia colours into list (RGB)
            # NOTE: min function - to use lowest sepia value & set max sepia value to 255
            sepiaRGB = [min(255, sepiaRed), min(255, sepiaGreen), min(255, sepiaBlue)]

            # Replacing canvas black img pixel w/ sepia pixel
            canvas[row][col] = sepiaRGB
  
    return canvas

def warmFilter(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])

    # Creating canvas (black img) to put newly created image on 
    canvas = cmpt120imageProjHelper.getBlackImage(width, height)

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # original Red, Blue, & Green colours of pixel
            ogRed = pixels[row][col][0]
            ogGreen = pixels[row][col][1]
            ogBlue = pixels[row][col][2]

        # Red - scaling up (checking red value)
            # IF original red value LESS THAN 64, scaled up value is (value/64)*80
            # IF original red value MORE THAN OR EQUAL 64,
                # scaled up value is (value-64)/(128-64)*(160-80)+80)
            # ELSE, scaled up value is (value-128)/(255-128) * (255-100) + 100
            if ogRed < 64:
                redScaleUp = int((ogRed/64)*80)

            elif (ogRed >= 64) and (ogRed < 128):
                redScaleUp = int((ogRed-64)/(128-64) * (160-80) + 80)
            else:
                redScaleUp = int((ogRed-128)/(255-128) * (255-160) + 160)

        # Blue - scaling down (checking blue value)
            # IF original blue value LESS THAN 64, scaled down value is (value/64)*50
            # IF original blue value MORE THAN OR EQUAL 64,
                # scaled down value is ((value-64)/(128-64)* (100-50)+50)
            # ELSE, scaled down value is (value-128)/(255-128) * (255-100) + 100)
            if ogBlue < 64:
                blueScaleDown = int((ogBlue/64)*50)
            elif (ogBlue >= 64) and (ogBlue < 128):
                blueScaleDown = int((ogBlue-64)/(128-64) * (100-50) + 50)
            else:
                blueScaleDown = int((ogBlue-128)/(255-128) * (255-100) + 100)
            
            # Creating Warm-Coloured Pixel: putting scaled colours & ogGreen colour in list
            warmRGB = [redScaleUp, ogGreen, blueScaleDown]
            # Replacing canvas black img pixel w/ warm-coloured pixel
            canvas[row][col] = warmRGB

    return canvas


# Apply Cold Filter
def coldFilter(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])

    # Creating canvas (black img) to put newly created image on 
    canvas = cmpt120imageProjHelper.getBlackImage(width, height)

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # original Red, Blue, & Green colours of pixel
            ogRed = pixels[row][col][0]
            ogGreen = pixels[row][col][1]
            ogBlue = pixels[row][col][2]

        # Red - scaling down (checking red value)
            # IF original red value LESS THAN 64, scaled down value is (value/64)*50
            # IF original red value MORE THAN OR EQUAL 64,
                # scaled down value is ((value-64)/(128-64)* (100-50)+50)
            # ELSE, scaled down value is (value-128)/(255-128) * (255-100) + 100)
            if ogRed < 64:
                redScaleDown = int((ogRed/64)*50)
            elif (ogRed >= 64) and (ogRed < 128):
                redScaleDown = int((ogRed-64)/(128-64) * (100-50) + 50)
            else:
                redScaleDown = int((ogRed-128)/(255-128) * (255-100) + 100)

        # Blue - scaling up (checking blue value)
            # IF original blue value LESS THAN 64, scaled up value is (value/64)*80
            # IF original blue value MORE THAN OR EQUAL 64,
                # scaled up value is (value-64)/(128-64)*(160-80)+80)
            # ELSE, scaled up value is (value-128)/(255-128) * (255-100) + 100
            if ogBlue < 64:
                blueScaleUp = int((ogBlue/64)*80)
            elif (ogBlue >= 64) and (ogBlue < 128):
                blueScaleUp = int((ogBlue-64)/(128-64) * (160-80) + 80)
            else:
                blueScaleUp = int((ogBlue-128)/(255-128) * (255-160) + 160)

            # Creating Cold-Coloured Pixel: putting scaled colours & ogGreen colour in list
            coldRGB = [redScaleDown, ogGreen, blueScaleUp]
            # Replacing canvas black img pixel w/ cold-coloured pixel
            canvas[row][col] = coldRGB

    return canvas

# Rotate Left
def rotateLeft(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])

    # "Rotated" Canvas Dimensions: switching height and width
    canvHeight = len(pixels[0])
    canvWidth = len(pixels)
    # Creating canvas (black img) to put newly created image on
    canvas = cmpt120imageProjHelper.getBlackImage(canvWidth, canvHeight)

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # Pixel's Row Number -(turns into)-> Canvas Col Number
                # e.g. Pixel Row -> Canvas Col (in 2x3 img) ITERATIONS
                #              0 -> 0
                #              0 -> 0
                #              0 -> 0
                #              1 -> 1
                #              1 -> 1
                #              1 -> 1
                # Therefore, no change

            # Pixel's Col Number -(turns into)-> Canvas Row Number, negative and + 1
                # e.g. Pixel Col -> Canvas Row (in 2x3 img) ITERATIONS
                #              0 -> -1
                #              1 -> -2
                #              2 -> -3
                # Therefore, from pattern, change is -(pixelcol + 1)

            # Replacing canvas black img pixel w/ img pixel
            canvas[-(col + 1)][row] = pixels[row][col]

    return canvas

# Rotate Right
def rotateRight(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])

    # "Rotated" Canvas Dimensions: switching height and width
    canvHeight = len(pixels[0])
    canvWidth = len(pixels)
    # Creating canvas (black img) to put newly created image on
    canvas = cmpt120imageProjHelper.getBlackImage(canvWidth, canvHeight)

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # Pixel's Row Number -(turns into)-> Canvas Col Number, negative & + 1
                # e.g. Pixel Row -> Canvas Col (in 2x3 img) ITERATIONS
                #             -1 -> 0
                #             -1 -> 0
                #             -1 -> 0
                #             -2 -> 1
                #             -2 -> 1
                #             -2 -> 1
                # Therefore, from pattern, change is -(pixelrow + 1)

            # Pixel's Col Number -(turns into)-> Canvas Row Number
                # e.g. Pixel Col -> Canvas Row (in 2x3 img) ITERATIONS
                #             -1 -> -1
                #             -2 -> -2
                #             -3 -> -3
                # Therefore, no change

            # Replacing canvas black img pixel w/ img pixel
            canvas[col][-(row + 1)] = pixels[row][col]

    return canvas

def doubleSize(pixels):
  # Height and width of image
  height = len(pixels)
  width = len(pixels[0])
  # Defines black image and times width and height by 2 (4 times)
  black = cmpt120imageProjHelper.getBlackImage(width*2,height*2)
  # Loop the original width and height. 
  # For every iteration, save the original pixel at the current loop index to the new image at:
  for row in range(height):
    for col in range(width):
      # result[0][0] same R/G/B values pixel at orginal[0][0]
      # Twice loop index for both x and y
      black[2*row][2*col] = pixels[row][col]
      # result[1][0] same R/G/B values pixel at orginal[0][0]
      # Twice loop index for x, twice loop index for y plus 1
      black[(2*row) + 1][2*col] = pixels[row][col]
      # result[0][1] same R/G/B values pixel at orginal[0][0]
      # Twice loop index for y, twice loop index for x plus 1
      black[2*row][(2*col)+1] = pixels[row][col]
      # result [1][1] same R/G/B values pixel at orginal[0][0]
      # Twice loop index plus 1 for both x and y
      # (perform four saves each iteration)
      black[(2*row)+1][(2*col)+1] = pixels[row][col]
  return black

# Half size
def halfSize(pixels):
  # Height and width of image
  height = len(pixels)
  width = len(pixels[0])
  # Defines black image and divides width and height by 2 (1/4 times)
  black = cmpt120imageProjHelper.getBlackImage(int(width/2),int(height/2))
  # Loop the new width and height
  for row in range(height):
    for col in range(width):
      # original[0][0]
      pixels1 = pixels[int(row)][int(col)] 
      # original[1][0]
      pixels2 = pixels[int(row-1)][int(col)] 
      # original[0][1]
      pixels3 = pixels[int(row)][int(col-1)] 
      # original[1][1]
      pixels4 = pixels[int(row-1)][int(col-1)] 
      # Save the average of the four indexing position for r, g and b
      # Indexes four times but saves once each iteration
      ave_r = int((pixels1[0] + pixels2[0] + pixels3[0] + pixels4[0])/4)
      ave_g = int((pixels1[1] + pixels2[1] + pixels3[1] + pixels4[1])/4)
      ave_b = int((pixels1[2] + pixels2[2] + pixels3[2] + pixels4[2])/4)
      # Retrives half size black image with average r/g/b
      black[int(row/2)][int(col/2)] = [ave_r, ave_g, ave_b]
  return black

def greenBox(rowList, colList, pixels):
    maxRow = max(rowList)
    minRow = min(rowList)
    maxCol = max(colList)
    minCol = min(colList)

    # Green Pixel: to replace pixels from img to a green pixel
    greenPixel = [0, 255, 0]

    # To indicate that the black image canvas is the pixels value
    canvas = pixels

    # Visual Example of how row & col ranges were chosen:
    #                minCol:       :maxCol
    #            (left side)       (right side)
    #                       0 1 2 3
    #   minRow:(top side)  0
    #                      1
    #                      2
    # maxRow:(bottom side) 3 

    # LEFT side (minimum value of columns)
    for row in range(minRow, maxRow + 1):
        for col in range(minCol, minCol + 1, 1):
            canvas[row][col] = greenPixel

    # RIGHT side (maximum value of columns)
    for row in range(minRow, maxRow + 1):
        for col in range(maxCol, maxCol + 1, 1):
            canvas[row][col] = greenPixel

    # TOP side (minimum value of rows)
    for row in range(minRow, minRow + 1):
        for col in range(minCol, maxCol + 1, 1):
            canvas[row][col] = greenPixel

    # BOTTOM side (maximum value of rows)
    for row in range(maxRow, maxRow + 1):
        for col in range(minCol, maxCol + 1, 1):
            canvas[row][col] = greenPixel

    return canvas

    # return (minRow, maxRow, minCol, maxCol)

def locateFish(pixels):
    # Image Dimensions: inspecting img for height & width
    height = len(pixels)
    width = len(pixels[0])

    # Creating canvas (black img) to put newly created image on
    canvas = cmpt120imageProjHelper.getBlackImage(width, height)

    # List of Row & Col values that meet yellow hsv parameters
    rowList = []
    colList = []

    # Nested For Loop: accessing each individual pixel
    for row in range(height):
        for col in range(width):
            # Replacing canvas black img pixel w/ img pixel
            canvas[row][col] = pixels[row][col]

            # separate RGB of pixel
            r = pixels[row][col][0]
            g = pixels[row][col][1]
            b = pixels[row][col][2]

            # HSV list of pixel [h, s, v]
            pixel_hsv = list(cmpt120imageProjHelper.rgb_to_hsv(r, g, b))
            # separate HSV of pixel
            h = pixel_hsv[0]
            s = pixel_hsv[1]
            v = pixel_hsv[2]

         # Detecting Yellow Pixels
            # tested values in hsv website: https://alloyui.com/examples/color-picker/hsv.html
            
            # Explanation: if the pixel's hue, saturation, & value meet the parameters below,
            #   - the pixel is considered a part of the fish's yellow body
            #   - & it's location (row, col) is added to the list of rows and cols

            # if h >= 50 and h <= 80:
            # if h >= 50 and h <= 65 and (s >= 20) and v >= 20:
            if (50 <= h <= 70) and (s >= 50) and (v >= 55):
                rowList.append(row)
                colList.append(col)

    fishGBox = greenBox(rowList, colList, pixels)

    return fishGBox