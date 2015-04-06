from PIL import Image
import cv2
import numpy as np
import sys
from copy import deepcopy
import cv2
import rs
 
key=raw_input("enter the key : ")
#print type(key)
message = raw_input("Enter the message :")
#print "the message is  "+message
#first_xor=key[0]^key[1]
length=len(key)
c=0
key_value=0
for z in range(0,length):
    key_value=(ord(key[c]))^key_value
    c=c+1
print "THE KEY VALUE IS " , key_value
key_value_binary="{0:b}".format(key_value)
print "THE FINAL KEY ",
print key_value_binary
v=0
#key_value=204
for x in range(0,len(message)):
    encoded_value=(ord(message[v])) ^ key_value
    v=v+1
print encoded_value
print "{0:b}".format(encoded_value)
coder=rs.RSCoder(20,10)
c=coder.encode(str(encoded_value))
#c=c-oder.encode("{0:b}".format(encoded_value))
p=[]
z=str(c)
print len(z)
for w in z:
    p.append(ord(w))
print p




