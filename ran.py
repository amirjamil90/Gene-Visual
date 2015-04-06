import numpy as np
import cv2
#d=np.loadtxt('hi.txt')
#f=np.shape(d)
#n=f[0]*f[1]
m=3.9885
n=5
#cv2.imwrite('aq.png',d)
global v
k=0
x=0.000000000000000
a = []
wz=[242,23,125,180,103]
lp=0
wzx=[]
'''
for g in range(f[0]):
      for h in range(f[1]):
            wz.insert(lp,d[g][h])
            lp=lp+1
print "the program beginss---------\n"
'''
print wz
'''for g in range(n):
      wz.insert(g,g)
'''
#wz=np.array(wz,dtype=int)
    
def s():
      v=0.4321
      for k in range(0,n):
       x=m*v*(1-v)
       a.insert(k,x)
       v=x

      
def shuf1(a,n):
    perm_index_a=[]
    b=a[:]
    #print len(a)
    #print len(b)
    #print a
    a.sort()
    sort_a=a[:]
    #print sort_arr
    #print a
    for k1 in range(0,n):
        t=sort_a[k1]
        for k2 in range(0,n):
            if(t==b[k2]):
                perm_index_a.insert(k1,k2)
                break
    print "the permutation index-------------------\n"            
    print perm_index_a

    # SHUFFLING BEGINS------------------------
    
    outnew=[0]*n
    
    for z in range(0,n):
          print perm_index_a[z],wz[z]
          #outnew.insert(perm_index_a[z],wz[z])
          outnew[perm_index_a[z]]=wz[z]
    #print "the original array\n"      
    #print wz
    print "the new shuffled array ----------------- \n"      
    print outnew
    gh=0
    ls=[]
    '''
    for g in range(f[0]):
      for h in range(f[1]):
            ls[g]]=outnew[gh]
            gh=gh+1
    ls=np.array(ls)
    cv2.imwrite('encode.png',ls)
    '''
    # deshuflling begins ---------------------
    
    decode_shuf=[]
    
    #outnew=np.array(outnew)
    
    for z in range(0,n):
     decode_shuf.insert(z,outnew[perm_index_a[z]])
    print "decoded array-----------------" 

    
    print decode_shuf
    #print decode_shuf == wzx 
    

    
if __name__=="__main__": 
    s()
    shuf1(a,n)
