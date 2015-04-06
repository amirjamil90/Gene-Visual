from PIL import Image
import cv2
import numpy as np
import sys
from copy import deepcopy
img=cv2.imread('obama2.jpg')
img_pix = img[:,:].tolist()
z_trans=map(list,zip(*img_pix))
print len(z_trans)


m=3.9885
global v
k=0
x=0.000000000000000
x_row=0.000000000000000
a = []
a_row=[]
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


def shuf1(a,n):

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
          outnew[perm_index_a[z]]=z_trans[z]
    z_trans2=map(list,zip(*outnew))
    y=np.asarray(z_trans2)
    cv2.imwrite("test5.png",y)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    print "column shuffling done"

def s_row():
    img=cv2.imread('test5.png')
    img_pix2 = img[:,:].tolist()
    n=len(img_pix2)
    v=0.4321
    for k in range(0,n):
      x_row=m*v*(1-v)
      a_row.insert(k,x_row)
      v=x_row    

def shuf2(a_row,n):

    img=cv2.imread('test5.png')
    img_pix2 = img[:,:].tolist()
    
    n=len(img_pix2)

    perm_index_a=[]
    b=a_row[:]
    a_row.sort()
    sort_a=a_row[:]
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

    print outnew
    y=np.asarray(outnew)
    cv2.imwrite("test8.png",y)
    print "row shuffling done"
      
w=0    
s(len(z_trans))
shuf1(a,len(z_trans))
s_row()
print a_row
shuf2(a_row,w)