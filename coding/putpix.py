import cv2
import random
import numpy as np
img=cv2.imread("jmi.jpg",0)
#print img
#np.savetxt('small.txt',img)
#cv2.show(img)
shape = img.shape
row = shape[0]
col = shape[1]
#x=np.loadtxt('smallchk.txt')
#cv2.imwrite("imageank.png",x)
#cv2.waitkey(0)
fp=open("encr.txt","w")
arr=[]

for i in range(row):
    for j in range(col):
        #print img[i][j]
        v=(str)(img[i][j])+" "
        arr.append(img[i][j])
        fp.write(v)
    fp.write("\n")
print img.size,len(arr)
if img.size==len(arr):
    print "success"
else:
    print "failure"
#print(arr)
