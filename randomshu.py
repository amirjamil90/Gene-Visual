import numpy as np
import cv2
import random
img=cv2.imread("monk_encrypt.png",0)
np.savetxt('shuf1.txt',img)
x=np.loadtxt('shuf1.txt')
print x
def shuffle(arr):
    a=len(arr)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      arr[d],arr[e]=arr[e],arr[d]
    return arr
arr=[1,2,3,4,5,6,6,7,7,5,4,5,6,65,4,3,5,4,34,534,343,6,6,5,445,45,45,65,334]
def shuf():
  n=29
  l=3.9885
  p=0.4321
  for k in range(1,n):
    c=l*p*(1-p)
    arr(k)=c
    p=c
  print arr


if __name__ == "__main__":
    z=shuffle(x)
    cv2.imwrite('shuff1.png',z)
