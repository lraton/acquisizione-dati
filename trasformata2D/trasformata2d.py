#!/home/leonardo/Programs/python_env/bin/python3


import matplotlib.pyplot as plt
from scipy import signal,fft
import numpy as np
from PIL import Image


path_to_img = 'line_30deg.png'

img = Image.open(path_to_img)
img.convert('RGB')
width, height = img.size



def getRGBvalues(image, mode='rgb'):
    rgbvalues = []
    for x in range(0, width):
        for y in range(0, height):
                rgbvalues.append(image.getpixel((x,y)))           
    if 'r' == mode:
        return rgbvalues[:,0]
    elif 'g' == mode:
        return rgbvalues[:,1]
    elif 'b' == mode:
        return rgbvalues[:,2]
    else:
        return rgbvalues
    

#scarto un canale 
red_channel = getRGBvalues(img)[:,0]
# freq = fft.rfftfreq(len(red_channel),1./fs)
print(red_channel)

# fft_red = fft.rftt(red_channel)






