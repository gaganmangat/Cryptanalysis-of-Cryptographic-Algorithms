

import random 

def binary_to_alphabet(b):
     ans=""
     alpha="fghijklmnopqrstu"
     for i in range(0,64,4):
         ind=int(b[i:i+4],2)
         ans+=alpha[ind] 
     #print(ans)
     return ans

def rand_key(p): 
	
	key1 = "" 

	
	for i in range(p): 
		
		temp = str(random.randint(0, 1)) 

		key1 += temp 
		
	return(key1) 

n = 64
f = open("plaintexts.txt","a")
val=int(0x0000901010005000)
#generating 100000 random binary plaintexts
count=0  
for i in range(100000):  
  str1 = rand_key(n) 
  f.write(str1+"\n")
  count+=1
  str1 = bin(val^int(str1,2))[2:]
  str1 = (64-len(str1))*'0' + str1
  f.write(str1+"\n")
  count+=1

print(count)  
f.close()  

#convert binary to alphabet
f1=open("plaintexts.txt","r")
lines=f1.readlines()     
f2=open("plaintexts1.txt","a")

for x in lines:
	f2.write(binary_to_alphabet(x)+"\n")
    
f1.close()
f2.close()


#create commands file plaintext.sh
f1=open("plaintext.sh","a")
f2=open("plaintexts1.txt","r")
lines=f2.readlines()
for s in lines:
    f1.write(s)
    f1.write("c\n")

f1.close()
f2.close()