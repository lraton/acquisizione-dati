#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft
import scipy.fft
from scipy.ndimage import gaussian_filter
from scipy.ndimage import median_filter
import numpy as np
from PIL import Image

##### Eserczio 1
imgs = ["line_45deg.png"]

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
    plt.title('Spectrum shift '+path_to_img)
    plt.colorbar()

    # Magnitude spectrum
    magnitude_spectrum = np.log(abs(fft2)+1)

    # Plot the magnitude spectrum
    plt.figure(figsize=(6, 6))
    plt.imshow(magnitude_spectrum)
    plt.title('Spectrum senza shift '+path_to_img)
    plt.colorbar()

plt.show()