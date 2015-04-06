from PIL import Image
import sys
import cv2
import hashlib
import rs,rsa
import numpy as np
import random
rowstride = 255
x=np.loadtxt('reed.txt')
r=str(x)
global signa
pubkey=rsa.PublicKey(11480060456748007523835064941328580064805863222076835592665701498626460611302141918251595045259022275115378154527348049014018676101117805257448811531453787, 65537)
privkey=rsa.PrivateKey(11480060456748007523835064941328580064805863222076835592665701498626460611302141918251595045259022275115378154527348049014018676101117805257448811531453787, 65537, 5297290206639249515972598667786404469838322011975305326118123792971341305581493511087015261944383036870856937146402441329496981768409514206571316532062993, 6695999916070553788087198710526758994630148877255684251404807367511363647665240457, 1714465442150857621418573490449635374350469483254021679683981914252714691)
signa=rsa.sign(r,privkey,'SHA-1')
po=open("orig.txt","w")
po.write(str(signa))
po.close()
signa=signa+'0'*191
nb=open("original_signa.txt","w")
nb.write(str(signa))
#val=rsa.verify(r, signa,pubkey)
#print val
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
decode_shuf=[]

def si(length):
  v=0.4321
  n=length
  for k in range(0,n):
    x=m*v*(1-v)
    a.insert(k,x)
    v=x
  sys.stderr.write("\nend of s function going to shuf and permute index \n ")



def shuf1(a,n,output_filename):
    """f=open("output.txt","w")
       f.write(str(output))
    f.close()"""
    shuf1_arr=[]
    perm_index_a=[]
    b=a[:]
    #sys.stderr.write(str(output))
    for i in output:
      for j in i:
        shuf1_arr.append(j)

    #sys.stderr.write(str(shuf1_arr))
    sys.stderr.write('length of shuf1_arr '+str(len(shuf1_arr)))
    sys.stderr.write("in shuf and permute index \n ")
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
    #l=output[0]
    #output[0]=l[:200]+'\0'*55
    #sys.stderr.write("the permutation index-------------------\n")
    #sys.stderr.write(str(perm_index_a))

    # SHUFFLING BEGINS------------------------

    outnew=[0]*n
    final_encrypt=[]
    for z in range(0,n):
          #print perm_index_a[z],output[z]
          #outnew.insert(perm_index_a[z],wz[z])
          outnew[perm_index_a[z]]=shuf1_arr[z]

    #sys.stderr.write(str(outnew))
    sys.stderr.write('length of outnew array---> '+str(len(outnew)))
    blocknum=0
    while True:
        if blocknum*255 > len(outnew):
            break
        rowdata = outnew[blocknum*255:(blocknum+1)*255]
        #sys.stderr.write('\nrowdata is------> '+str(rowdata))
        x="".join(rowdata)
        blocknum += 1
        final_encrypt.append(x)
        #sys.stderr.write(x)
        #sys.stderr.write('\nlength of x is------>'+str(len(x)))
        #break

    #sys.stderr.write(str(final_encrypt))
    #sys.stderr.write(str(len(final_encrypt)))
    final_encrypt=final_encrypt[:-1]
        #sys.stdout.write(str(decoded))
    #sys.stderr.write("the new shuffled array ----------------- \n")
    out = Image.new("L", (rowstride,len(final_encrypt)))
    out.putdata("".join(final_encrypt))
    out.save(output_filename)

    #deshuffling


    #outnew=np.array(outnew)

    """for z in range(0,n):
     decode_shuf.insert(z,outnew[perm_index_a[z]])
    print "decoded array-----------------"
    f=open("output-per.txt","w")
    f.write(str(decode_shuf))
    f.close()"""

    #print decode_shuf

    #sys.stderr.write(str(outnew))




def encode(input, output_filename):
    #print privkey
    #signa=rsa.sign(r,privkey,'SHA-1')
    coder = rs.RSCoder(255,223)
    #sig='2'*200+signa[-55:]
    #signa_hex=repr(signa)
    output.append(signa)
    #print "hello"
    #a=1
    block=1
    count=1
    while block:
        block = input.read(223)
        #print "hello"
        #if not block: break
        code = coder.encode(block)
        """if count==1:
          code=code[:250]+'\0'*5
          count+=1"""
        output.append(code)
        sys.stderr.write(".")

    sys.stderr.write("\n")
    n=len(output)
    print n
    n=n*255
    si(n)
    shuf1(a,n,output_filename)

    out = Image.new("L", (rowstride,len(output)))
    out.putdata("".join(output))
    out.save('monk-r.png')

    #cv2.imwrite("new_enc.png",ad)
#def deshuf(input):


sign=""


def shuf2(a,n):

    perm_index_a=[]
    b=a[:]
    a.sort()
    sort_a=a[:]
    #print len(sort_a)
    #print a
    for k1 in range(0,n):
        t=sort_a[k1]
        for k2 in range(0,n):
            if(t==b[k2]):
                perm_index_a.insert(k1,k2)
                break
    return perm_index_a



def decode(input_filename):
    data1=[]
    input = Image.open(input_filename)
    data = "".join(chr(x) for x in input.getdata())
    del input
    blocknum=0
    while True:
        if blocknum*255 >= len(data):
            break
        rowdata = data[blocknum*255:(blocknum+1)*255]
        #sys.stderr.write('\nrowdata is------> '+str(rowdata))
        blocknum += 1
        #sys.stdout.write(str(decoded))
        #sys.stderr.write(".")
        data1.append(rowdata)
    n=len(data1)*255
    sys.stderr.write('\n'+str(len(data1)))
    """f=open("n.txt","w")
    f.write(str(data1))
    f.close()"""
    si(n)
    perm_index_a=shuf2(a,n)
    sys.stderr.write('\nlength of perm_index in decode--> '+str(len(perm_index_a)))
    data1_break=[]
    for i in data1:
        for j in i:
            data1_break.append(j)
    #sys.stderr.write('\n'+str(data1_break))
    #sys.stderr.write('\nlength of data1_break--> '+str(len(data1_break)))

    for z in range(0,n):
      decode_shuf.insert(z,data1_break[perm_index_a[z]])
    #print "decoded array-----------------"

    sys.stderr.write('\nlength of decode_shuf--> '+str(len(decode_shuf)))
    final_decrypt=[]

    blocknum=0
    while True:
        if blocknum*255 >= len(decode_shuf):
            break
        rowdata = decode_shuf[blocknum*255:(blocknum+1)*255]
        #sys.stderr.write('\nrowdata is------> '+str(rowdata))
        x="".join(rowdata)
        blocknum += 1
        final_decrypt.append(x)
        #sys.stderr.write(x)
        #sys.stderr.write('\nlength of x is------>'+str(len(x)))
        #break
    sys.stderr.write('\nlength of final_decrypt is------> '+str(len(final_decrypt)))
    coder = rs.RSCoder(255,223)

    sign = final_decrypt[0]
    t=open("original_signa_decoded.txt","w")
    t.write(str(sign))
    t.close()

    #sys.stderr.write(str(sign))
    data = final_decrypt[1:]
    #sys.stderr.write(str(data))

    for i in data:
        decoded = coder.decode(i)
        sys.stdout.write(str(decoded))
        sys.stderr.write(".")
    #f=open("chksign.txt","w")
    sys.stderr.write("\n")
    #u.close()"""
    """val=rsa.verify(r,sign,pubkey)
    s=str(val)
    sys.stderr.write(s)"""


if __name__ == "__main__":
    if "-d" == sys.argv[1]:
        # decode
        decode(sys.argv[2])
        #check()


    else:
        # encode
        encode(sys.stdin,sys.argv[1])
