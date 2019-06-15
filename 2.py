# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:36:49 2017

@author: SUIKI
"""
import numpy as np 
import cv2

def main():
    img =cv2.imread("Error1.jpg")
    h,w =img.shape[:2]
    for i in range(1,h-1):
        for j in range(1,w-1):
            f=img[i,j]
            #print (f)
            a=f&
if __name__ == '__main__':
    main()

