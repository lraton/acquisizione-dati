#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft
import scipy.fft
from scipy.ndimage import gaussian_filter
from scipy.ndimage import median_filter
import numpy as np
from PIL import Image


path_to_img = 'line_60deg.png'

img = Image.open(path_to_img)
img=img.convert('RGB')
width, height = img.size
   

#scarto un canale 
red_channel, green_channel, blue_channel = img.split()

fft2 = scipy.fft.fft2(red_channel, s=None, axes=(- 2, - 1), norm=None, 
               overwrite_x=False, workers=None, plan=None)

fft_result_shifted = scipy.fft.fftshift(fft2)

# Compute the magnitude spectrum
spectrum = np.log(abs(fft_result_shifted)+1)

# Plot the magnitude spectrum
plt.figure(figsize=(6, 6))
plt.imshow(spectrum)
plt.title('Spectrum '+path_to_img)
plt.colorbar()





#####
path_to_img = 'saltandpepper_lena.jpg'
img = Image.open(path_to_img)
img = img.convert('RGB')
plt.figure(figsize=(6, 6))
plt.title(path_to_img)
plt.imshow(img)

plt.colorbar()
width, height = img.size

#scarto un canale 
red_channel, green_channel, blue_channel = img.split()

fft2 = scipy.fft.fft2(red_channel, s=None, axes=(- 2, - 1), norm=None, 
               overwrite_x=False, workers=None, plan=None)

fft_result_shifted = scipy.fft.fftshift(fft2)

# Compute the magnitude spectrum
spectrum = np.log(abs(fft_result_shifted)+1)

radius = 50  # Adjust the radius as needed
mask = np.zeros((width, height))
center_x, center_y = width // 2, height // 2
for x in range(width):
    for y in range(height):
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            mask[x, y] = 1

magnitude_mask = spectrum * mask

# Plot the spectrum with mask
plt.figure(figsize=(6, 6))
plt.imshow(magnitude_mask)
plt.title('Spectrum with mask'+path_to_img)
plt.colorbar()


# Plot the Gaussian Filter
gaussian=gaussian_filter(red_channel, sigma=1)

plt.figure(figsize=(6, 6))
plt.imshow(gaussian)
plt.title('gaussian Filter '+path_to_img)
plt.colorbar()

# Plot the Median filter
median=median_filter(red_channel, size=20)
plt.figure(figsize=(6, 6))
plt.imshow(median)
plt.title('Median filter '+path_to_img)
plt.colorbar()
plt.show()




