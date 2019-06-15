# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:17:48 2018

@author: SUIKI
"""
from PIL import Image
import reverse


def main():
    
    img1 =Image.open('koala.bmp')
    img2 =Image.open('bird.bmp')
    #img1.show()
    New1 =Image.open('Aerial.bmp')
    New2 =Image.open('Lenna.bmp')
    New1_array =New1.load()
    New2_array =New2.load()
    img1_array =img1.load()
    img2_array =img2.load()
    
    
    h,w =img1.size
    for i in range (h):
        for j in range (w):          
            
            f =img1_array[i,j]
            R1 =(f[0]>>4)<<4
            G1 =(f[1]>>4)<<4
            B1 =(f[2]>>4)<<4
            
            g =img2_array[i,j]
            R2 =reverse.reverse(g[0])
            G2 =reverse.reverse(g[1])
            B2 =reverse.reverse(g[2])
            
            r1=R1|R2
            g1=G1|G2
            b1=B1|B2       
            
            New1_array[i,j]=(r1,g1,b1)
            m =img1_array[i,j]
            n =New1_array[i,j]    
            
            eR =m[0]-n[0]
            eG =m[1]-n[1]
            eB =m[2]-n[2]
            
            R3 =(g[0]>>4)<<4
            G3=(g[1]>>4)<<4
            B3 =(g[2]>>4)<<4
            
            R4 =reverse.reverse(f[0])
            G4 =reverse.reverse(f[1])
            B4 =reverse.reverse(f[2])
            
            r2=R3|R4
            g2=G3|G4
            b2=B3|B4       
            
            New2_array[i,j]=(r2,g2,b2)
            
            m2 =img2_array[i,j]
            n2 =New2_array[i,j]    
            
            eR2 =m2[0]-n2[0]
            eG2 =m2[1]-n2[1]
            eB2 =m2[2]-n2[2]
            
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
        
            if j+1 < w:
                right =img1_array[i,j+1]
                rR =right[0]+rightR
                rG =right[1]+rightG
                rB =right[2]+rightB
            if i+1 < h and j+1 < w:
                rightbottom =img1_array[i+1,j+1]
                rbR =rightbottom[0]+rightbottomR
                rbG =rightbottom[1]+rightbottomG
                rbB =rightbottom[2]+rightbottomB
            if i+1 < h:    
                bottom =img1_array[i+1,j]
                bR =bottom[0]+bottomR
                bG =bottom[1]+bottomG
                bB =bottom[2]+bottomB
                
            if i+1 < h and j-1 >= 0:
                leftbottom =img1_array[i+1,j-1]  
                lbR =leftbottom[0]+leftbottomR
                lbG =leftbottom[1]+leftbottomG
                lbB =leftbottom[2]+leftbottomB
            
            if j+1 < w:
                img1_array[i,j+1] =(rR,rG,rB)
            if i+1 < h and j+1 < w:
                img1_array[i+1,j+1] =(rbR,rbG,rbB)
            if i+1 < h:
                img1_array[i+1,j] =(bR,bG,bB)
            if i+1 < h and j-1 >= 0:
                img1_array[i+1,j-1] =(lbR,lbG,lbB)
            
            rightR2 =int(7.0/16*eR2)
            rightbottomR2 =int(1.0/16*eR2)
            bottomR2 =int(5.0/16*eR2)
            leftbottomR2 =int(3.0/16*eR2)
            
            rightG2 =int(7.0/16*eG2)
            rightbottomG2 =int(1.0/16*eG2)
            bottomG2 =int(5.0/16*eG2)
            leftbottomG2 =int(3.0/16*eG2)
            
            rightB2 =int(7.0/16*eB2)
            rightbottomB2 =int(1.0/16*eB2)
            bottomB2 =int(5.0/16*eB2)
            leftbottomB2 =int(3.0/16*eB2)
        
            if j+1 < w:
                right2 =img2_array[i,j+1]
                rR2 =right2[0]+rightR2
                rG2 =right2[1]+rightG2
                rB2 =right2[2]+rightB2
            if i+1 < h and j+1 < w:
                rightbottom2 =img2_array[i+1,j+1]
                rbR2 =rightbottom2[0]+rightbottomR2
                rbG2 =rightbottom2[1]+rightbottomG2
                rbB2 =rightbottom2[2]+rightbottomB2
            if i+1 < h:
                bottom2 =img2_array[i+1,j]
                bR2 =bottom2[0]+bottomR2
                bG2 =bottom2[1]+bottomG2
                bB2 =bottom2[2]+bottomB2
            if i+1 < h and j-1 >= 0:
                leftbottom2 =img2_array[i+1,j-1]
                lbR2 =leftbottom2[0]+leftbottomR2
                lbG2 =leftbottom2[1]+leftbottomG2
                lbB2 =leftbottom2[2]+leftbottomB2
            
            if j+1 < w:
                img2_array[i,j+1] =(rR2,rG2,rB2)
            if i+1 < h and j+1 < w:
                img2_array[i+1,j+1] =(rbR2,rbG2,rbB2)
            if i+1 < h:
                img2_array[i+1,j] =(bR2,bG2,bB2)
            if i+1 < h and j-1 >= 0:
                img2_array[i+1,j-1] =(lbR2,lbG2,lbB2)
            
        
            
            pass
    #print (img1_array[23,56],img2_array[23,56],New1_array[23,56])        
    New1.save('Error1.bmp')
    New2.save('Error2.bmp')
    
    #New1.show()
    #New2.show()
            
            
            

if __name__ == '__main__':
    main()
