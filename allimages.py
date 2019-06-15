# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os


def getAllImages(color):
    assert os.path.exists(color)
    assert os.path.isdir(color)
    imageList = os.listdir(color)
    imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(color, item))]
    return imageList

    print getAllImages(r"C:\Software\PythonDoc\color\color") 