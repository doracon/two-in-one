# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 00:07:13 2017

@author: inoue
"""

#from skimage import data, img_as_float
#import skimage.measure
#from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_ssim as ssim
from skimage import img_as_float
from PIL import Image
import cv2

def main():

    im1 =img_as_float(Image.open('koala.bmp'))
    im2 =img_as_float(Image.open('New1.bmp'))
    im3 =img_as_float(Image.open('Error1.bmp'))

    ''' 
    print("compare sources and result without error diffusion ")
    print(ssim(im1,im2,multichannel=True))
    
    print("compare sources and result with error diffusion ")
    print(ssim(im1,im3,multichannel=True))
    print("\n")
    '''
    
    kernel_size = (5, 5)
    sigma = 1.5
    im1 = cv2.GaussianBlur(im1, kernel_size, sigma)
    im2 = cv2.GaussianBlur(im2, kernel_size, sigma)
    im3 = cv2.GaussianBlur(im3, kernel_size, sigma)
    #cv2.imwrite('Error1r.png',im3)
    
    
    print("compare sources and result without error diffusion(with gaussian filter)")
    print(ssim(im1,im2,multichannel=True))
    
    print("compare sources and result with error diffusion(with gaussian filter)")
    print(ssim(im1,im3,multichannel=True))

    pass


if __name__ == '__main__':
    main()

