# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:17:48 2018

@author: SUIKI
"""
from PIL import Image
import numpy as np
import reverse


def new():
    img1 =Image.open('koala.bmp')
    img2 =Image.open('bird.bmp')
    #img1.show()
    New1 =Image.open('koala.bmp')
    New1_array =New1.load()
    
    h,w =img1.size
    for i in range(h):
        for j in range(w):          
            img1_array =img1.load()
            f =img1_array[i,j]
            R1 =(f[0]>>4)<<4
            G1 =(f[1]>>4)<<4
            B1 =(f[2]>>4)<<4
            
            img2_array =img2.load()
            g =img2_array[i,j]
            R2 =reverse.reverse(g[0])
            G2 =reverse.reverse(g[1])
            B2 =reverse.reverse(g[2])
            
            r1=R1|R2
            g1=G1|G2
            b1=B1|B2       
            
            New1_array[i,j]=(r1,g1,b1)
            
    #print (img1_array[23,56],img2_array[23,56],New1_array[23,56])   
            
            
            
            
   
   
    New1.save('new1.bmp')
    #New1.show()

if __name__ == '__main__':
    new()
