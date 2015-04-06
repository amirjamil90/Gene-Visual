''' -------------------------------  code by MOHMMAD AMR JAMIL  AND ANKUR SALDHI ------------------------------   '''

'''------------------------IMPORTING PACKAGES--------------'''

from copy import deepcopy
from PIL import Image
import cv2
import numpy as np
import sys
from copy import deepcopy
import cv2
import rs

''' KEY AND MESSAGE INPUT '''

key=raw_input("enter the key : ")
message = raw_input("Enter the message :")
length=len(key)

c=0
key_value=0

'''----------------------PEROFRMING OPERATION ON KEY------------------- '''

for z in range(0,length):
    key_value=(ord(key[c]))^key_value
    c=c+1

print "THE KEY VALUE IS " , key_value

key_value_binary = "{0:b}".format(key_value)

print "THE FINAL KEY ",
print key_value_binary
'''---------------------ENCODING OF DATA --------------------------''' 
v=0
#key_value=204
for x in range(0,len(message)):
    encoded_value=(ord(message[v])) ^ key_value
    v=v+1

print encoded_value

print "{0:b}".format(encoded_value)

'''-----------------------REED SOLOMON ENCODER -----------------------------'''

coder=rs.RSCoder(20,10)

code=coder.encode(str(encoded_value))
#c=c-oder.encode("{0:b}".format(encoded_value))
p=[]
z=str(code)


'''----------------------HIDING THE DATA BEHIND THE IMAGE------------------------------'''

img=cv2.imread('obama2.jpg')
row,col = img.shape[0],img.shape[1]
img_pix = img[:4,:6].tolist()
print img_pix





#http://ideone.com/4xQtbW,http://repl.it/hEn
def mapp(y):
    a = 3.999
    x= y * (1-y)
    x=(10000000000*x)
    x=int(x)
    x=x/10000000000.0
    x = x*a
    x=(10000000000*x)
    x=int(x)
    x=x/10000000000.0
    return x
 
monitor,num = 10000,[]

#text = raw_input('Enter the text to hide: ')
#key = raw_input('Enter the key: ')
key = 'ankur'
text=z

x = 0
for each_char in key:
    x+=ord(each_char)-64
#print x
x = 1.0/x
x=(10000000000*x);
x=int(x);
x=x/10000000000.0;
#print x
for i in range(len(text)):
    x = mapp(x)
    itr = int(monitor * x)
 
    for j in range(itr):
        x = mapp(x)
    #print x
    num.append(int(x * 3))
 
#print 'num is',num

#print 'text is',text
#print row,col
#for index,item in num:

count,flag = 0,0
for i in img_pix:
    for j in i:
        j[num[count]] = ord(text[count])
        count+=1
        if count >= len(text):
            flag = 1
            break

    if flag == 1:
        break

print img_pix


'''----------------------APPLYING GENETIC ALGORITHM COLUMN SHUFFLING TO THE OBTAINED STEGO IMAGE-------------------------'''



img3=cv2.imread('obama2.jpg')
img_pix3 = img3[:,:].tolist()

#TAKING THE TRANSPOSE OF THE IMAGE 
z_trans=map(list,zip(*img_pix3))
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

'''-----------------------------OBTAINING THE PERMUTATION INDEX-------------------------------- '''

def s(length):
  v=0.4321
  n=length
  for k in range(0,n):
    x=m*v*(1-v)
    a.insert(k,x)
    v=x

'''--------------------------------APPLYING THE SHUFFLING ALGORITHM------------------------------------------'''
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
    final_encrypt=[]
    for z in range(0,n):
          outnew[perm_index_a[z]]=z_trans[z]
    z_trans2=map(list,zip(*outnew))
    y=np.asarray(z_trans2)
    cv2.imwrite("test5.png",y)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    print "column shuffling done"



'''-----------------------------APPLYING THE ROW SHUFFLING ALGORITHM------------------------------''' 

def s_row():
    img=cv2.imread('test5.png')
    img_pix2 = img[:,:].tolist()
    n=len(img_pix2)
    v=0.4321
    for k in range(0,n):
      x_row=m*v*(1-v)
      a_row.insert(k,x_row)
      v=x_row    

'''--------------------------------SHUFFLING THE ROW -----------------------------'''
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

img3=cv2.imread('test8.png')
img_pix3 = img3[:6,:4].tolist()
print img_pix3



    
    





    
