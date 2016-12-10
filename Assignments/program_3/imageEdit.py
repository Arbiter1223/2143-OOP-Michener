from PIL import Image
import sys
from io import BytesIO
import urllib.request
import random
#import main

class ImageEd(object):
    def __init__(self, file):
        # Open image
        self.img = Image.open(file)
        # Get width and height
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    def glass_effect(self, distance):
        # Loop through image
        for xpos in range(self.width):
            for ypos in range(self.height):
                # Get a list of x-coordinate numbers using "distance" as radius
                nums = [x for x in range(xpos - distance, xpos + distance)]
                valid = False
                # Choose a random x-coordinate from the list; only accept x-coordinates of numbers actually in the image
                while valid == False:
                    x = random.choice(nums)
                    if x in range(0, self.width):
                        valid = True
                # Get a list of y-coordinate numbers using "distance" as radius
                nums = [y for y in range(ypos - distance, ypos + distance)]
                valid = False
                # Choose a random y-coordinate from the list; only accept y-coordinates of numbers actually in the image
                while valid == False:
                    y = random.choice(nums)
                    if y in range(0, self.height):
                        valid = True
                # Get a neighbor pixel using randomly generated coordinates above
                neighbor = self.img.getpixel((x,y))
                # Set pixel, move on to next
                self.img.putpixel((xpos,ypos), neighbor)

    def flip(self):
        # Loop through half of image; we don't need to flip it twice...
        for x in range(self.width):
            # For y in half the height
            for y in range(int(self.height / 2)):
                # Set opposite y-coordinate
                opposite = self.height - (y + 1)
                # Get pixels from opposite y-coordinates and same x-coordinate
                rgb1 = self.img.getpixel((x,y))
                rgb2 = self.img.getpixel((x,opposite))
                # Swap pixels, move on to next pair
                self.img.putpixel((x,opposite), rgb1)
                self.img.putpixel((x,y), rgb2)

    def blur(self, kernal):
        #***WARNING: may take a while to render!***
        # Loop through entire image
        for xpos in range(self.width):
            for ypos in range(self.height):
                # Create 2 lists for valid pixel coordinates within kernal
                validxpos = []
                validypos = []
                # Add x-coordinate numbers in range of kernal
                nums = [x for x in range(xpos - kernal, xpos + kernal)]
                for x in nums:
                    # Only add numbers if they're actually in image
                    if x in range(0, self.width):
                        validxpos.append(x)
                # Add y-coordinate numbers in range of kernal
                nums = [y for y in range(ypos - (kernal + 1), ypos + (kernal + 1))]
                for y in nums:
                    # Only add numbers if they're actually in image
                    if y in range(0, self.height):
                        validypos.append(y)
                # Initialize variables
                reds = 0
                greens = 0
                blues = 0
                colors = 0
                # Loop through all valid pixels in kernal, add all color values together, keep counter of how many pixels there are
                for y in validypos:
                    for x in validxpos:
                        rgb = self.img.getpixel((x, y))
                        reds += rgb[0]
                        greens += rgb[1]
                        blues += rgb[2]
                        colors += 1
                # Average all the colors
                averageRed = int(reds / colors)
                averageGreen = int(greens / colors)
                averageBlue = int(blues / colors)
                # Create average color to be used in the blur process
                averageRGB = (averageRed, averageGreen, averageBlue)
                # Set current pixel to blurred pixel
                self.img.putpixel((xpos,ypos), averageRGB)
                # Clear the lists, move on to next pixel
                validxpos.clear
                validypos.clear

    def posterize(self, snap):
        # Loop through entire image
        for x in range(self.width):
            for y in range(self.height):
                # Get the current pixel
                rgb = self.img.getpixel((x,y))
                # Split the individual color values up
                oldRed = rgb[0]
                oldGreen = rgb[1]
                oldBlue = rgb[2]
                # Create different "color bins" using snap variable
                binRed = oldRed % snap
                binGreen = oldGreen % snap
                binBlue = oldBlue % snap
                # Use Red bin to modify red color
                if binRed < (snap // 2):
                    newRed = oldRed - binRed
                else:
                    newRed = oldRed + (snap - binRed)
                # Use Green bin to modify green color
                if binGreen < (snap // 2):
                    newGreen = oldGreen - binGreen
                else:
                    newGreen = oldGreen + (snap - binGreen)
                # Use Blue bin to modify blue color
                if binBlue < (snap // 2):
                    newBlue = oldBlue - binBlue
                else:
                    newBlue = oldBlue + (snap - binBlue)
                # Set new color to binned colors
                newColor = (newRed, newGreen, newBlue)
                # Set current pixel to new color, move on to next pixel
                self.img.putpixel((x,y), newColor)

    def solarize(self, threshold):
        # Loop through entire image
        for x in range(self.width):
            for y in range(self.height):
                # Get current pixel
                rgb = self.img.getpixel((x,y))
                # Split the pixel into the individual colors
                red = rgb[0]
                green = rgb[1]
                blue = rgb[2]
                # Negate colors if above specified threshold
                if red > threshold:
                    red = 255 - red
                if green > threshold:
                    green = 255 - green
                if blue > threshold:
                    blue = 255 - blue
                # Set new pixel color with modified values
                newRGB = (red, green, blue)
                # Set pixel to new color, move on to next pixel
                self.img.putpixel((x,y), newRGB)

    def warhol(self):
        # Grayscale image with additional function
        self.grayscale()
        # Posterize with snap value of 32
        self.posterize(32)
        # This makes 8 shades of gray (plus pure white, for a total of 9 different intervals)

        # Loop through entire image
        for x in range(self.width):
            for y in range(self.height):
                # Get individual pixel
                rgb = self.img.getpixel((x, y))
                # Get intensity value
                intensity = rgb[0]

                # Choose color depending on which "bin" the intensity falls into
                if intensity == 0:
                    # Blue
                    newColor = (0, 0, 255)
                elif intensity == 32:
                    # Yellow
                    newColor = (255, 255, 0)
                elif intensity == 64:
                    # Red
                    newColor = (255, 0, 0)
                elif intensity == 96:
                    # Green
                    newColor = (0, 255, 0)
                elif intensity == 128:
                    # Cyan
                    newColor = (0, 255, 255)
                elif intensity == 160:
                    # Purple
                    newColor = (255, 0, 255)
                elif intensity == 192:
                    # Orange
                    newColor = (255, 128, 0)
                elif intensity == 224:
                    # Pink
                    newColor = (255, 0, 128)
                elif intensity == 255:
                    # White
                    newColor = (255, 255, 255)
                # Set pixel to selected color, move on to next pixel
                self.img.putpixel((x,y), newColor)

    def showImage(self):
        # Saves image to temporary file, opens with default OS image viewer
        self.img.show()

    def example(self):
        # Function bassed off of example from github
        # Inverts colors
        # Loop through entire image
        for x in range(self.width):
            for y in range(self.height):
                # Get pixel from image
                rgb = self.img.getpixel((x,y))
                # Split pixel into individual color values
                red = rgb[0]
                green = rgb[1]
                blue = rgb[2]
                # Invert each color value
                invertedRed = 255 - red
                invertedGreen = 255 - green
                invertedBlue = 255 - blue
                # Make new color with new color values
                rgb2 = (invertedRed, invertedGreen, invertedBlue)
                # Set pixel to new color, move on to next pixel
                self.img.putpixel((x,y), rgb2)

    def grayscale(self):
        # Loop through entire image
        for x in range(self.width):
            for y in range(self.height):
                # Get current pixel
                rgb = self.img.getpixel((x, y))
                # Split pixel into individual color variables
                red = rgb[0]
                green = rgb[1]
                blue = rgb[2]
                # Find "Grayness" of image
                # Based off of the Grayscale class from Study Guide 2
                # Find gray via lightness, average, and luminosity
                lightness = int(((max(red, green, blue) + min(red, green, blue)) / 2))
                average = int((red + green + blue) / 3)
                luminosity = int((0.21 * red) + (0.72 * green) + (0.07 * blue))
                # To really make it gray, average those values together
                self.grayValue = int((lightness + average + luminosity) / 3)
                # Make new color with gray values
                self.grayColor = (self.grayValue, self.grayValue, self.grayValue)
                # Set pixel to gray color, move on to next pixel
                self.img.putpixel((x, y), self.grayColor)