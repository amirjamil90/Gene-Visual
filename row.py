from PIL import Image
import cv2
import numpy as np
import sys
from copy import deepcopy
img=cv2.imread('test5.png')
img_pix = img[:,:].tolist()
#z_trans=map(list,zip(*img_pix))
#print len(z_trans)


m=3.9885
global v
k=0
x=0.000000000000000
a = []
wz=[]
lp=0
wzx=[]
outnew=[]
output = []


def s(length):
  v=0.4321
  n=length
  for k in range(0,n):
    x=m*v*(1-v)
    a.insert(k,x)
    v=x

def shuf2(a,n):

    img=cv2.imread('test5.png')
    print img
    img_pix2 = img[:,:].tolist()
    n=len(img_pix2)
    print n
    #img2=cv2.imread('test1.jpg')
    #img_pix2 = img2[:,:].tolist()
    perm_index_a=[]
    b=a[:]
    a.sort()
    sort_a=a[:]
    for k1 in range(0,n):
        t=sort_a[k1]
        for k2 in range(0,n):
            if(t==b[k2]):
                perm_index_a.insert(k1,k2)
                break
    outnew=[0]*n
    outnew2=[0]*n
    final_encrypt=[]
    for z in range(0,n):
          outnew[perm_index_a[z]]=img_pix2[z]
    #z_trans2=map(list,zip(*outnew))
    y=np.asarray(outnew)
    cv2.imwrite("test4.png",y)
    print "row shuffling done"
      
s(len(img_pix))
shuf2(a,len(img_pix))

