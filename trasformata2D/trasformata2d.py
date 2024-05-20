#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft
import numpy as np
from PIL import Image

import cv2

class Filter2D():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.mask = self.getMask()

    def getMask(self):
        radius = 50  # Adjust the radius as needed
        mask = np.zeros((self.width, self.height))
        center_x, center_y = self.width // 2, self.height // 2
        for x in range(self.width):
            for y in range(self.height):
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                    mask[x, y] = 1
        return mask
        


path_to_img = 'saltandpepper_lena.jpg'

img = Image.open(path_to_img)

width, height = img.size



def getRGBvalues(image, mode='rgb'):
    image = image.convert('RGB')
    rgbvalues = []
    for x in range(0, width):
        for y in range(0, height):
                rgbvalues.append(image.getpixel((x,y)))  
                print(image.getpixel((x,y)))         
    if 'r' == mode:
        return [i[0] for i in rgbvalues]
    elif 'g' == mode:
        return [i[1] for i in rgbvalues]
    elif 'b' == mode:
        return [i[2] for i in rgbvalues]
    else:
        return rgbvalues
    

#scarto un canale 
red_channel = getRGBvalues(img, 'r')
print(red_channel)

red_channel = np.array(red_channel).reshape(width,height) 

# # Display the magnitude of the Fourier Transform
# cv2.imshow('Fourier Transform', red_channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#calcolo la fft, shifto le 
fourier = fft.fft2(red_channel)
shift = fft.fftshift(fourier)
print(shift)
no_shift_magnitude = np.log(abs(fourier)+1) 
magnitude = np.log(abs(shift)+1)

filter = Filter2D(width, height)
filtered = shift*filter.mask
filtered_magnitude = np.log(abs(filtered)+1)

plt.figure("Not shifted")
plt.imshow(no_shift_magnitude)
plt.title("Not shifted")

plt.figure("Filtered")
plt.title("Filtered")
plt.imshow(magnitude)

plt.figure("Shifted")
plt.title("Shifted")
plt.imshow(filtered_magnitude)
plt.show()






