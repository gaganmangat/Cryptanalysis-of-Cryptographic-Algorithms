import collections
from collections import defaultdict
import math
from collections import Counter
import sys

def alphabet_to_binary(s):
    ans=""
    alpha="fghijklmnopqrstu"
    for x in s:
       z=bin(alpha.index(x))[2:]
       z= (4-len(z))*'0' + z 
       ans+=z 
    #print(ans)   
    return ans


f1=open("output.txt","r")
lines=f1.readlines()
f2=open("ciphertext.txt","a")



i=0
while i<len(lines):
    if lines[i]=='Slowly, a new text starts appearing on the screen. It reads ...\n':
        i+=2
        f2.write(alphabet_to_binary(lines[i].strip())+"\n")
    else:
       i+=1   


f1.close()
f2.close()






