# -*- coding: utf-8 -*-
"""
Created on Wed May  9 19:49:38 2018

@author: SUIKI
"""
from PIL import Image
import numpy as np

def error(n,file):
    
    img1 =Image.open(file)
    h,w =img1.size
    for i in range(1,h-1):
        for j in range(1,w-1):   
            
            img1_array =img1.load()
            m =img1_array[i,j]
    
            eR =m[0]-n[0]
            eG =m[1]-n[1]
            eB =m[2]-n[2]
                
            rightR =int(7.0/16*eR)
            rightbottomR =int(1.0/16*eR)
            bottomR =int(5.0/16*eR)
            leftbottomR =int(3.0/16*eR)
            
            rightG =int(7.0/16*eG)
            rightbottomG =int(1.0/16*eG)
            bottomG =int(5.0/16*eG)
            leftbottomG =int(3.0/16*eG)
            
            rightB =int(7.0/16*eB)
            rightbottomB =int(1.0/16*eB)
            bottomB =int(5.0/16*eB)
            leftbottomB =int(3.0/16*eB)
        
            right =img1_array[i,j+1]
            rightbottom =img1_array[i+1,j+1]
            bottom =img1_array[i+1,j]
            leftbottom =img1_array[i+1,j-1]
            
            rR =right[0]+rightR
            rG =right[1]+rightG
            rB =right[2]+rightB
            
            rbR =rightbottom[0]+rightbottomR
            rbG =rightbottom[1]+rightbottomG
            rbB =rightbottom[2]+rightbottomB
            
            bR =bottom[0]+bottomR
            bG =bottom[1]+bottomG
            bB =bottom[2]+bottomB
            
            lbR =leftbottom[0]+leftbottomR
            lbG =leftbottom[1]+leftbottomG
            lbB =leftbottom[2]+leftbottomB
            
            img1_array[i,j+1] =(rR,rG,rB)
            img1_array[i+1,j+1] =(rbR,rbG,rbB)
            img1_array[i+1,j] =(bR,bG,bB)
            img1_array[i+1,j-1] =(lbR,lbG,lbB)
            
            pass
    


if __name__ == '__error__':
    error(n,file)
    
