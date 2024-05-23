#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft
import scipy.fft
from scipy.ndimage import gaussian_filter
from scipy.ndimage import median_filter
import numpy as np
from PIL import Image

##### Eserczio 1
imgs = ["line_0deg.png", "line_30deg.png", "line_60deg.png", "line_90deg.png", "line_0deg.png"]

# Itera attraverso ogni immagine nell'elenco
for immagine in imgs:
    path_to_img = immagine #path_to_img = immagine

    img = Image.open(path_to_img)
    img=img.convert('RGB')
    width, height = img.size
    

    #Isolo i canali 
    red_channel, green_channel, blue_channel = img.split()

    #Trasformata 2d
    fft2 = scipy.fft.fft2(red_channel)

    #Shift
    fft_result_shifted = scipy.fft.fftshift(fft2)

    # Magnitude spectrum
    magnitude_spectrum = np.log(abs(fft_result_shifted)+1)

    # Plot the magnitude spectrum
    plt.figure(figsize=(6, 6))
    plt.imshow(magnitude_spectrum)
    plt.title('Spectrum '+path_to_img)
    plt.colorbar()


##### Eserczio 2
path_to_img = "lena_std.tif"
img = Image.open(path_to_img)
img = img.convert('RGB')
plt.figure(figsize=(6, 6))
plt.title(path_to_img)
plt.imshow(img)

plt.colorbar()
width, height = img.size

#scarto un canale 
red_channel, green_channel, blue_channel = img.split()

fft2 = scipy.fft.fft2(red_channel)

fft_result_shifted = scipy.fft.fftshift(fft2)

# Compute the magnitude spectrum
magnitude_spectrum = np.log(abs(fft_result_shifted)+1)

#Mask
radius = 50
mask = np.zeros((width, height))
center_x, center_y = width // 2, height // 2
for x in range(width):
    for y in range(height):
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            mask[x, y] = 1

spectrum_mask = magnitude_spectrum * mask

# Plot the spectrum with mask
plt.figure(figsize=(6, 6))
plt.imshow(spectrum_mask)
plt.title('Spectrum with mask '+path_to_img)
plt.colorbar()


##### Esercizio 3
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

fft2 = scipy.fft.fft2(red_channel)

fft_result_shifted = scipy.fft.fftshift(fft2)

# Compute the magnitude spectrum
magnitude_spectrum = np.log(abs(fft_result_shifted)+1)

radius = 50  # Adjust the radius as needed
mask = np.zeros((width, height))
center_x, center_y = width // 2, height // 2
for x in range(width):
    for y in range(height):
        if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
            mask[x, y] = 1

spectrum_mask = magnitude_spectrum * mask

# Plot the spectrum with mask
plt.figure(figsize=(6, 6))
plt.imshow(spectrum_mask)
plt.title('Spectrum with mask '+path_to_img)
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




