#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft, ndimage
import numpy as np
from PIL import Image

import cv2


class CircleFilter2D():
    def __init__(self, radius, width, height) -> None:
        self.radius = radius
        self.width = width
        self.height = height
        self.mask = self.getMask()

    def getMask(self):
        radius = self.radius  # Adjust the radius as needed
        mask = np.zeros((self.width, self.height))
        center_x, center_y = self.width // 2, self.height // 2
        for x in range(self.width):
            for y in range(self.height):
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                    mask[x, y] = 1
        return mask


path_to_img = 'saltandpepper_lena.jpg'

img = Image.open(path_to_img)
img= img.convert('RGB')
width, height = img.size

#scarto un canale 
red_channel, green_channel, blue_channel= img.split()

# # Display the magnitude of the Fourier Transform
# cv2.imshow('Fourier Transform', red_channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#calcolo la fft, shifto le 
fourier = fft.fft2(red_channel)
shift = fft.fftshift(fourier)
no_shift_magnitude = np.log(abs(fourier)+1) 
magnitude = np.log(abs(shift)+1)

filter = CircleFilter2D(50,width, height)
filtered = shift*filter.mask
filtered_magnitude = np.log(abs(filtered)+1)

gaussian_filtered = ndimage.gaussian_filter(red_channel,2) 

median_filtered = ndimage.median_filter(red_channel, size= 20) 

unshift = fft.ifftshift(filtered)
filtered_img = fft.ifft2(unshift)
filtered_img = np.abs(filtered_img)

norm_data = (filtered_img - np.min(filtered_img)) / (np.max(filtered_img) -np.min(filtered_img))
scaled_data = (norm_data*255).astype(np.uint8)
scaled_arr = scaled_data

# new_img = Image.new('RGB', (width,height))
color = [[(i, 0, 0)] for i in scaled_data]
prova = np.full((height,width), 300)
print(prova)

image_array = np.array(prova)
new_img = Image.fromarray(image_array)
new_img.show()


plt.figure("Not shifted")
plt.imshow(no_shift_magnitude)
plt.title("Not shifted")
plt.figure("Filtered")
plt.title("Filtered")
plt.imshow(magnitude)

plt.figure("Shifted")
plt.title("Shifted")
plt.imshow(filtered_magnitude)

plt.figure("Gaussian Filtered")
plt.title("Gaussian Filtered")
plt.imshow(gaussian_filtered)

plt.figure("Median Filtered")
plt.title("Median Filtered")
plt.imshow(median_filtered)

plt.show()






