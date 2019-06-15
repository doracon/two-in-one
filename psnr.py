# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:36:19 2018

@author: SUIKI
"""
from PIL import Image
import numpy
import math

def psnr(img1,img2):
    
    img1 =Image.open('Lenna.bmp')
    img2 =Image.open('New1.bmp')
    img1_array =img1.load()
    img2_array =img2.load()
    mse = numpy.mean( (img1_array - img2_array) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
  
if __name__ == '__main__':
    psnr()
