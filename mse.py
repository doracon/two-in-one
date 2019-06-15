# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:48:56 2018

@author: SUIKI
"""

from PIL import Image
import numpy
import math
import matplotlib.pyplot as plt
import cv2
#导入你要测试的图像
im = numpy.array (Image.open ('koala.bmp'),'f')#将图像1数据转换为float型
im2 = numpy.array (Image.open ('New1.bmp'),'f')#将图像2数据转换为float型
#print (im.shape,im.dtype)
#图像的行数
height = im.shape[0]
#图像的列数
width = im.shape[1]

kernel_size = (5, 5)
sigma = 1.5
im = cv2.GaussianBlur(im, kernel_size, sigma)
im2 = cv2.GaussianBlur(im2, kernel_size, sigma)

#提取R通道
r = im[:,:,0]
#提取g通道
g = im[:,:,1]
#提取b通道
b = im[:,:,2]
#打印g通道数组
#print (g)
#图像1,2各自分量相减，然后做平方；
R = im[:,:,0]-im2[:,:,0]
G = im[:,:,1]-im2[:,:,1]
B = im[:,:,2]-im2[:,:,2]
#做平方
mser = R*R
mseg = G*G
mseb = B*B
#三个分量差的平方求和
a1 = r*r
a2 = g*g
a3 = b*b

SUM = mser.sum() + mseg.sum() + mseb.sum()
SUM2 = a1.sum() + a2.sum() + a3.sum()
MSE = SUM / (height * width * 3)
PSNR = 10*math.log ( (255.0*255.0/(MSE)) ,10)
SNR = 10*math.log ( ((SUM2)/(SUM)) ,10)

print (MSE)
print (SNR)
#im = numpy.array (Image.open ('onion.bmp'))#无符号型
#im2 = numpy.array (Image.open ('New1.bmp'))
#plt.subplot (121)#窗口1
#plt.title('origin image')
#plt.imshow(im,plt.cm.gray)

#plt.subplot(122)#窗口2
#plt.title('rebuilt image')
#plt.imshow(im2,plt.cm.gray)
#plt.show()
