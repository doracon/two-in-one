# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:39:21 2018

@author: SUIKI
"""

from PIL import Image
import numpy as np

def reverse(m):
    
    m =((m&0x55)<<1)|((m&0xAA)>>1)
    m =((m&0x33)<<2)|((m&0xCC)>>2)
    m =((m&0x0F)<<4)|((m&0xF0)>>4)
    m =(m<<4)&255
    m =m>>4
    return m
    
if __name__ == '__reverse__':
    reverse()

    