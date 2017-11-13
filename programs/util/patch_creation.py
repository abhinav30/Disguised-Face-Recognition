#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:05:37 2017

@author: chinmay
"""

import cv2
import numpy as np
import sys
import os



fp=open('allpaths.txt','r')

for image_path in fp:
    image_path=image_path.strip('\n')
    

#    image_path= '/home/chinmay/Desktop/SMAI_project/Visible_cropped/P1/P1_2.jpeg'
#    print (os.path.exists(image_path))

#print (image_path)
    l=[]
    l=image_path.split('/')
    x=len(l)
    h=l[x-1].split('.')
    g=h[0]
    img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
#    fp=open('img1.txt','w')
    
    count=1
    for i in range(1,6):
        for j in range(1,6):
            h[0]=g
            t=str(count)
            t='_'+t
            h[0]=h[0]+t
            h[0]=h[0]+'.txt'
            h[0]='patches/'+h[0]
            fw=open(h[0],'w')
            for n in range(((i-1)*30),(i*30)):
                for m in range(((j-1)*26),(j*26)):
#                    print (img[n][m],end='')
#                    print (" ",end='')
                     temp=img[n][m]
                     t=str(temp)
                     fw.write(t)
                     if m!=((j*26)-1):
                         fw.write(",")
                fw.write('\n')
            count+=1
    
#    img=img.tolist()
#    for item in img:
#        str1 = ','.join(str(e) for e in item)
#        str1=str1+'\n'
#        fp.write(str1)
    
        
#    
    

