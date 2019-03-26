#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:43:10 2018

@author: dataquanty
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:28:09 2018

@author: dataquanty
"""


import numpy as np
from math import sqrt, pi, acos,cos
from matplotlib import pyplot as plt
from scipy.misc import imsave
from bisect import bisect_left
import matplotlib.animation as animation

h , w = 1000, 1000
img = np.ones((h,w))


center = (500,500)
r = [20,80,200,300,400,500,600]
r = np.exp(range(1,8)).astype(int)
lagval = [0,pi,0,pi,0,pi,0]
maxd = 810
r = range(10,maxd,20)
lagval = [0,pi]*int(len(r)/2)

lagval = np.random.rand(len(r))*pi
lagval = [-pi/4,pi/3]*int(len(r)/2)
#lagval = [0,0.05]*int(len(r)/2)
lagval = [0,pi]*int(len(r)/2)

def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


for i in range(h):
    for j in range(w):
        if (i,j) == center:
            img[i][j]=0
        
        else: 
            d = dist((i,j),center)
            k = bisect_left(list(r),d) 
            
            
            #dist((i,j),center)<= r1:
            val = (j-center[1])/d
            img[i][j] = cos(acos(val)-lagval[k])
            """
            angle = acos((j-center[1])/dist((i,j),center))
            if i > center[0]:
                angle = 2*pi - angle
            val = ((angle - lagrad)%(2*pi))/2*pi
            img[i][j] = val
            """


#imsave('figLag_pi_s2.png',img)
fig = plt.figure()
plt.figure(figsize=(10,10))       
im = plt.imshow(img,cmap='gray',animated=True)

def updatefig(*args):
    global lagval, r, center
    updval = np.random.rand(len(r))*pi/8 - pi/4
    updval = np.array([pi/8,-pi/8]*int(len(r)/2))
    lagval = lagval + updval
    for i in range(h):
        for j in range(w):
            if (i,j) == center:
                img[i][j]=0
            
            else: 
                d = dist((i,j),center)
                k = bisect_left(list(r),d) 
                val = (j-center[1])/d
                img[i][j] = cos(acos(val)-lagval[k])
    im.set_array(img)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, frames=100, blit=True)
Writer = animation.ImageMagickFileWriter(fps=10)
#writer = Writer(fps=15, bitrate=1800)
ani.save('anim.mp4',writer=Writer)
#interpolation='nearest'
plt.show()