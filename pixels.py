from PIL import Image
"""im = Image.open('lena.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
#print pixel_values"""


import cv2
import numpy as np
img = cv2.imread('lena.png')
#print img.dtype
#img.shape[0] * img.shape[1] = img.size
#print img[0][1],img[0][2]
print img.shape[0],img.shape[1],img.size
x= img[:,:].tolist()
print type(x)
print x    #first row