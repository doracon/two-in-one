# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:30:20 2018

@author: SUIKI
"""

from PIL import Image
import numpy as np
import reverse2

def main():
    
    img =Image.open('New1.bmp')
    img_array =img.load()
    
    im =Image.open('Error2.bmp')
    im_array =im.load()
    
    test =Image.open('Error2.bmp')
    test_array=test.load()
    h,w =img.size
    for i in range(1,h-1):
        for j in range(1,w-1):  
            f =img_array[i,j]
            R =reverse2.reverse2(f[0])
            G =reverse2.reverse2(f[1])
            B =reverse2.reverse2(f[2])
            test_array[i,j]=(R,G,B)
            pass
    
    #print (img_array[22,55],im_array[22,55],test_array[22,55])
    test.save('test1.bmp')
    #test.show()
    
if __name__ == '__main__':
    main()