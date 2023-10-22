# AES Algorithm uses a single common secret key to encrypt and decrypt the data
# and is used by governments due to its high level of data integrity. 
# The encryption and decryption occur in blocks where the data is modified and stored
# in blocks of size 128 bits, whereas the size of the encryption key can be 128, 192, or 256 bits.

import pyaes

# The key and text are entered and encoded into bytes. The key should be 32 bytes(256 bits),
#  or else, an error will be thrown
key = input("Enter a key of 32bits: ").encode('utf-8')
text = input("Enter the text to be encrypted: ").encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)

# Encrypting the text
encryptedData = aes.encrypt(text)
print("The encrypted data of the text is: ", encryptedData)

# Decrypting the encrypted text 
aes = pyaes.AESModeOfOperationCTR(key)
decryptedData = aes.decrypt(encryptedData)

print("Decryptint the text ", decryptedData.decode())