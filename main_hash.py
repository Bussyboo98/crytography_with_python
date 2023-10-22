# Hashlib module is a collection of hashing algorithms used to encrypt data as a hash.
# Regardless of the size of the data, a hash is a string of fixed length.

import hashlib

text = input("Enter text to be encrypted: ").encode()

#SHA256 – Secure Hash Algorithm converts the data into a fixed string of 256 bytes in length. 
#It improves security, as longer hashes lead to higher security levels. It is the successor of SHA1 algorithms.
encryptedData = hashlib.sha256(text)

# Converting the encrypted text into a hexadecimal
encryption = encryptedData.hexdigest()
print(encryption)

# This encoding technique is used widely by tech giants as the data encrypted is almost impossible to decrypt.