# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:43:37 2018

@author: SUIKI
"""


from PIL import Image
import numpy as np

def reverse2(f):
    
    f =((f&0x55)<<1)|((f&0xAA)>>1)
    f =((f&0x33)<<2)|((f&0xCC)>>2)
    f =((f&0x0F)<<4)|((f&0xF0)>>4)
    return f

    
    
if __name__ == '__reverse2__':
    reverse2()
