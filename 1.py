# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:35:22 2017

@author: SUIKI
"""
from PIL import Image
import numpy as np  
import matplotlib.pyplot as plt  
from skimage.measure import compare_ssim as ssim
from skimage import data,filters
import cv2

def main():
    ijpg = Image.open("Error1.png")
    ijpg.save('Error1.jpg', quality=100)
    ijpg0 = Image.open("Error2.png")
    ijpg0.save('Error2.jpg', quality=100)
    ijpg1 = Image.open("Koala.png")
    ijpg1.save('Koala.jpg', quality=100)
    ijpg2 = Image.open("Bird.png")
    ijpg2.save('Bird.jpg', quality=100)
     
    YssimA = [0]*7
    YssimB = [0]*7
    
    kList = [1,10,20,30,40,50,99]
    #for k in range(0,100):
    for k in kList:
        im = Image.open("Error1.jpg")
        im.save('Afp.jpg', quality=k)

        #imag = Image.open('fp.jpg')
        #imag.save('Afp.png')
        
        imag = cv2.imread('Afp.jpg')
        img = cv2.imread('Afp.jpg')
        
        h,w=imag.shape[:2]

        for i in range(1,h-1):
            for j in range(1,w-1):
                a1 = img[i,j]
                b1 = ((a1&0x55)<<1)|((a1&0xAA)>>1)
                c1 = ((b1&0x33)<<2)|((b1&0xCC)>>2)
                img[i,j] =((c1&0x0F)<<4)|((c1&0xF0)>>4)
                cv2.imwrite('Bfp.jpg',img)
        
            im1 = cv2.imread('Koala.jpg')
            im2 = cv2.imread('Error1.jpg')
            im3 = cv2.imread('Afp.jpg')
        
            kernel_size = (5, 5)
            sigma = 1.5
            im1 = cv2.GaussianBlur(im1, kernel_size, sigma)
            im2 = cv2.GaussianBlur(im2, kernel_size, sigma)
            im3 = cv2.GaussianBlur(im3, kernel_size, sigma)
         
            img1 = cv2.imread('Bird.jpg')
            img2 = cv2.imread('Error2.jpg')
            img3 = cv2.imread('Bfp.jpg')
            
            img1 = cv2.GaussianBlur(img1, kernel_size, sigma)
            img2 = cv2.GaussianBlur(img2, kernel_size, sigma)
            img3 = cv2.GaussianBlur(img3, kernel_size, sigma)
            
            #cv2.show(imag)
            #cv2.show()
        if k == kList[0]:
            cv2.imwrite('Afp0.jpg',imag)
            cv2.imwrite('Bfp0.jpg',img)
            YssimA[0]=ssim(im1,im3,multichannel=True)
            YssimB[0]=ssim(img1,img3,multichannel=True)
        if k == kList[1]:
            cv2.imwrite('Afp10.jpg',imag)
            cv2.imwrite('Bfp10.jpg',img)    
            YssimA[1]=ssim(im1,im3,multichannel=True)
            YssimB[1]=ssim(img1,img3,multichannel=True)
        if k == kList[2]:
            cv2.imwrite('Afp30.jpg',imag)
            cv2.imwrite('Bfp30.jpg',img)
            YssimA[2]=ssim(im1,im3,multichannel=True)
            YssimB[2]=ssim(img1,img3,multichannel=True)
        if k == kList[3]:
            cv2.imwrite('Afp50.jpg',imag)
            cv2.imwrite('Bfp50.jpg',img)
            YssimA[3]=ssim(im1,im3,multichannel=True)
            YssimB[3]=ssim(img1,img3,multichannel=True)
        if k == kList[4]:
            cv2.imwrite('Afp70.jpg',imag)
            cv2.imwrite('Bfp70.jpg',img)
            YssimA[4]=ssim(im1,im3,multichannel=True)
            YssimB[4]=ssim(img1,img3,multichannel=True)
        if k == kList[5]:
            cv2.imwrite('Afp90.jpg',imag)
            cv2.imwrite('Bfp90.jpg',img)
            YssimA[5]=ssim(im1,im3,multichannel=True)
            YssimB[5]=ssim(img1,img3,multichannel=True)
        if k == kList[6]:
            cv2.imwrite('Afp100.jpg',imag)
            cv2.imwrite('Bfp100.jpg',img)
            YssimA[6]=ssim(im1,im3,multichannel=True)
            YssimB[6]=ssim(img1,img3,multichannel=True)
            
    print("Af")
    print(ssim(im1,im2,multichannel=True))
    print("Bf")   
    print(ssim(img1,img2,multichannel=True))     
''' 
    labels = kList
    bar_width = 0.5
    plt.bar(np.arange(7), YssimA, label = 'ssimA', color = 'steelblue', alpha = 0.8, width = bar_width)
    plt.bar(np.arange(7)+bar_width, YssimB, label = 'ssimB', color = 'indianred', alpha = 0.8, width = bar_width)      
    plt.xlabel('CompressionRatio')
    plt.ylabel('SSIM')
    plt.xticks(np.arange(11)+bar_width,labels) 
    plt.ylim([0,1])
    for xssimA,yssimA in enumerate(YssimA): 
        plt.text(xssimA, yssimA+ 0.01, '%.6s'%yssimA) 
    for xssimB,yssimB in enumerate(YssimB): 
        plt.text(xssimB, yssimB+ 0.01, '%.6s'%yssimB) 
    plt.legend()
    plt.show() 
'''
    


if __name__ == '__main__':
    main()

